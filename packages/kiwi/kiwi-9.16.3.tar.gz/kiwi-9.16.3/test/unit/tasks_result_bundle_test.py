import sys
import mock
import os

from mock import patch, call

import kiwi

from .test_helper import raises, argv_kiwi_tests, patch_open
from kiwi.exceptions import KiwiBundleError
from kiwi.tasks.result_bundle import ResultBundleTask
from kiwi.system.result import Result


class TestResultBundleTask(object):
    def setup(self):
        sys.argv = [
            sys.argv[0], 'result', 'bundle', '--target-dir', 'target_dir',
            '--bundle-dir', 'bundle_dir', '--id', 'Build_42'
        ]
        self.abs_target_dir = os.path.abspath('target_dir')
        self.abs_bundle_dir = os.path.abspath('bundle_dir')
        self.context_manager_mock = mock.Mock()
        self.file_mock = mock.Mock()
        self.enter_mock = mock.Mock()
        self.exit_mock = mock.Mock()
        self.enter_mock.return_value = self.file_mock
        setattr(self.context_manager_mock, '__enter__', self.enter_mock)
        setattr(self.context_manager_mock, '__exit__', self.exit_mock)

        self.file_mock.read.return_value = b'data'

        self.xml_state = mock.Mock()
        self.xml_state.get_image_version = mock.Mock(
            return_value='1.2.3'
        )

        self.result = Result(self.xml_state)
        self.result.add(
            key='keyname', filename='filename-1.2.3',
            use_for_bundle=True, compress=True, shasum=True
        )

        kiwi.tasks.result_bundle.Help = mock.Mock(
            return_value=mock.Mock()
        )
        self.task = ResultBundleTask()

    def teardown(self):
        sys.argv = argv_kiwi_tests

    def _init_command_args(self):
        self.task.command_args = {}
        self.task.command_args['help'] = False
        self.task.command_args['bundle'] = False
        self.task.command_args['--target-dir'] = 'target_dir'
        self.task.command_args['--bundle-dir'] = 'bundle_dir'
        self.task.command_args['--id'] = 'Build_42'
        self.task.command_args['--zsync-source'] = None

    @raises(KiwiBundleError)
    def test_process_invalid_bundle_directory(self):
        self._init_command_args()
        self.task.command_args['--bundle-dir'] = \
            self.task.command_args['--target-dir']
        self.task.command_args['bundle'] = True
        self.task.process()

    @patch('kiwi.tasks.result_bundle.Result.load')
    @patch('kiwi.tasks.result_bundle.Command.run')
    @patch('kiwi.tasks.result_bundle.Path.create')
    @patch('kiwi.tasks.result_bundle.Path.which')
    @patch('kiwi.tasks.result_bundle.Compress')
    @patch('kiwi.tasks.result_bundle.Checksum')
    @patch('os.path.exists')
    @patch_open
    def test_process_result_bundle(
        self, mock_open, mock_exists, mock_checksum, mock_compress,
        mock_path_which, mock_path_create, mock_command, mock_load
    ):
        checksum = mock.Mock()
        compress = mock.Mock()
        mock_path_which.return_value = 'zsyncmake'
        compress.compressed_filename = 'compressed_filename'
        mock_compress.return_value = compress
        mock_checksum.return_value = checksum
        mock_exists.return_value = False
        mock_open.return_value = self.context_manager_mock
        mock_load.return_value = self.result
        self._init_command_args()
        self.task.command_args['bundle'] = True
        self.task.command_args['--zsync-source'] = 'http://example.com/zsync'

        self.task.process()

        mock_load.assert_called_once_with(
            os.sep.join([self.abs_target_dir, 'kiwi.result'])
        )
        mock_path_create.assert_called_once_with(self.abs_bundle_dir)
        assert mock_command.call_args_list == [
            call([
                'cp', 'filename-1.2.3',
                os.sep.join([self.abs_bundle_dir, 'filename-1.2.3-Build_42'])
            ]),
            call([
                'zsyncmake', '-e',
                '-u', 'http://example.com/zsync/compressed_filename',
                '-o', 'compressed_filename.zsync',
                'compressed_filename'
            ])
        ]
        mock_compress.assert_called_once_with(
            os.sep.join([self.abs_bundle_dir, 'filename-1.2.3-Build_42'])
        )
        mock_checksum.assert_called_once_with(
            compress.compressed_filename
        )
        checksum.sha256.assert_called_once_with()

    @patch('kiwi.logger.log.warning')
    @patch('kiwi.tasks.result_bundle.Result.load')
    @patch('kiwi.tasks.result_bundle.Command.run')
    @patch('kiwi.tasks.result_bundle.Path.create')
    @patch('kiwi.tasks.result_bundle.Path.which')
    @patch('kiwi.tasks.result_bundle.Compress')
    @patch('kiwi.tasks.result_bundle.Checksum')
    @patch('os.path.exists')
    @patch_open
    def test_process_result_bundle_zsyncmake_missing(
        self, mock_open, mock_exists, mock_checksum, mock_compress,
        mock_path_which, mock_path_create, mock_command, mock_load, mock_log
    ):
        checksum = mock.Mock()
        compress = mock.Mock()
        mock_path_which.return_value = None
        compress.compressed_filename = 'compressed_filename'
        mock_compress.return_value = compress
        mock_checksum.return_value = checksum
        mock_exists.return_value = False
        mock_open.return_value = self.context_manager_mock
        mock_load.return_value = self.result
        self._init_command_args()
        self.task.command_args['bundle'] = True
        self.task.command_args['--zsync-source'] = 'http://example.com/zsync'

        self.task.process()
        mock_log.assert_called_once_with(
            '--> zsyncmake missing, zsync setup skipped'
        )

    def test_process_result_bundle_help(self):
        self._init_command_args()
        self.task.command_args['help'] = True
        self.task.command_args['bundle'] = True
        self.task.process()
        self.task.manual.show.assert_called_once_with(
            'kiwi::result::bundle'
        )
