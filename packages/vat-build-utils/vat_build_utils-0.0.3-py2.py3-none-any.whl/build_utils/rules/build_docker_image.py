import logging
import os

import docker

from build_utils import docker_utils, utils

logger = logging.getLogger(__name__)

def build_docker_image(execution_context, path, name, tag=None, dockerfile=None):
    full_path = os.path.join(execution_context.dir_path, path)

    docker_client = docker.APIClient(version='auto')

    docker_build_context = docker_utils.create_build_context_archive(full_path)
    docker_build_context_hash = utils.compute_file_hash(docker_build_context)
    docker_build_context.seek(0)

    tag = tag if tag is not None else docker_build_context_hash

    image_registry = execution_context.build_context.get_image_registry()

    full_tag = image_registry.get_full_image_tag(name, tag)

    if not image_registry.has_image(name, tag):
        docker_utils.build_docker_image(
            docker_client,
            tag=full_tag,
            fileobj=docker_build_context,
            custom_context=True,
            dockerfile=dockerfile
        )

        image_registry.push_image(name, tag)

    else:
        logger.info("Image %s already exists in registry, skipping...", full_tag)

    return {
        "images": {
            name: full_tag
        }
    }
