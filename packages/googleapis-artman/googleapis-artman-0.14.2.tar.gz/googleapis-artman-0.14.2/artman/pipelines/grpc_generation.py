# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Pipelines that run gRPC codegen"""

from artman.pipelines import code_generation as code_gen
from artman.tasks import package_metadata_tasks
from artman.tasks import protoc_tasks
from artman.tasks import python_grpc_tasks
from artman.utils import task_utils


class GrpcClientPipeline(code_gen.CodeGenerationPipelineBase):

    def __init__(self, **kwargs):
        super(GrpcClientPipeline, self).__init__(
            get_grpc_task_factory(kwargs), **kwargs)


class ProtoClientPipeline(code_gen.CodeGenerationPipelineBase):

    def __init__(self, **kwargs):
        super(ProtoClientPipeline, self).__init__(
            get_proto_task_factory(kwargs), **kwargs)


class GrpcTaskFactoryBase(code_gen.TaskFactoryBase):

    def get_tasks(self, **kwargs):
        tasks = self.get_grpc_codegen_tasks(**kwargs)
        tasks += self._get_publish_tasks(**kwargs)
        return task_utils.instantiate_tasks(tasks, kwargs)

    def get_grpc_codegen_tasks(self, **kwargs):
        return []

    def get_validate_kwargs(self):
        return code_gen.COMMON_REQUIRED

    def get_invalid_kwargs(self):
        return []


class _RubyGrpcTaskFactory(GrpcTaskFactoryBase):

    def get_grpc_codegen_tasks(self, **kwargs):
        return [
            protoc_tasks.ProtoAndGrpcCodeGenTask,
            protoc_tasks.RubyGrpcCopyTask,
        ]


class _JavaGrpcTaskFactory(GrpcTaskFactoryBase):

    def get_grpc_codegen_tasks(self, **kwargs):
        return [
            protoc_tasks.ProtoDescGenTask,
            protoc_tasks.ProtoCodeGenTask,
            protoc_tasks.GrpcCodeGenTask,
            package_metadata_tasks.PackageMetadataConfigGenTask,
            package_metadata_tasks.ProtoPackageMetadataGenTask,
            package_metadata_tasks.GrpcPackageMetadataGenTask,
            protoc_tasks.JavaProtoCopyTask,
        ]

class _JavaProtoTaskFactory(GrpcTaskFactoryBase):

    def get_grpc_codegen_tasks(self, **kwargs):
        return [
            protoc_tasks.ProtoDescGenTask,
            protoc_tasks.ProtoCodeGenTask,
            package_metadata_tasks.PackageMetadataConfigGenTask,
            package_metadata_tasks.ProtoPackageMetadataGenTask,
            protoc_tasks.JavaProtoCopyTask,
        ]


class _PythonGrpcTaskFactory(GrpcTaskFactoryBase):

    def get_grpc_codegen_tasks(self, **kwargs):
        return [
            python_grpc_tasks.PythonChangePackageTask,
            protoc_tasks.ProtoDescGenTask,
            protoc_tasks.ProtoAndGrpcCodeGenTask,
            package_metadata_tasks.PackageMetadataConfigGenTask,
            python_grpc_tasks.PythonMoveProtosTask,
        ]


class _GoGrpcTaskFactory(GrpcTaskFactoryBase):
    """Responsible for the protobuf/gRPC flow for Go language."""

    def get_grpc_codegen_tasks(self, **kwargs):
        return [
            protoc_tasks.ProtoAndGrpcCodeGenTask,
            protoc_tasks.GoCopyTask,
        ]

    def get_validate_kwargs(self):
        return ['gapic_yaml', 'gapic_code_dir'] + code_gen.COMMON_REQUIRED


class _CSharpGrpcTaskFactory(GrpcTaskFactoryBase):

    def get_grpc_codegen_tasks(self, **kwargs):
        return [
            protoc_tasks.ProtoCodeGenTask,
            protoc_tasks.GrpcCodeGenTask,
        ]


class _PhpGrpcTaskFactory(GrpcTaskFactoryBase):

    def get_grpc_codegen_tasks(self, **kwargs):
        return [
            protoc_tasks.ProtoAndGrpcCodeGenTask,
            protoc_tasks.PhpGrpcRenameTask,
            protoc_tasks.PhpGrpcMoveTask,
        ]


class _NodeJsGrpcTaskFactory(GrpcTaskFactoryBase):

    def get_grpc_codegen_tasks(self, **kwargs):
        return [
            protoc_tasks.NodeJsProtoCopyTask,
        ]


GRPC_TASK_FACTORY_DICT = {
    'java': _JavaGrpcTaskFactory,
    'python': _PythonGrpcTaskFactory,
    'go': _GoGrpcTaskFactory,
    'ruby': _RubyGrpcTaskFactory,
    'php': _PhpGrpcTaskFactory,
    'csharp': _CSharpGrpcTaskFactory,
    'nodejs': _NodeJsGrpcTaskFactory,
}


PROTO_TASK_FACTORY_DICT = {
    'java': _JavaProtoTaskFactory,
}


def get_grpc_task_factory(kwargs):
    if 'language' not in kwargs:
        raise ValueError('Valid --language argument required for gRPC codegen')

    language = kwargs['language']
    cls = GRPC_TASK_FACTORY_DICT.get(language)
    if cls:
        return cls()
    else:
        raise ValueError('No gRPC task factory found for language: '
                         + language)


def get_proto_task_factory(kwargs):
    if 'language' not in kwargs:
        raise ValueError('Valid --language argument required for gRPC codegen')

    language = kwargs['language']
    cls = PROTO_TASK_FACTORY_DICT.get(language)
    if cls:
        return cls()
    else:
        raise ValueError('No proto task factory found for language: '
                         + language)
