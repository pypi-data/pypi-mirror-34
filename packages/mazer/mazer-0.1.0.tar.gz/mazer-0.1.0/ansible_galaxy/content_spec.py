import logging
import os

from ansible_galaxy import galaxy_content_spec
from ansible_galaxy import content_spec_parse
from ansible_galaxy.models.content_spec import ContentSpec

log = logging.getLogger(__name__)


def is_scm(content_spec_string):
    if '://' in content_spec_string or '@' in content_spec_string:
        return True

    return False


# FIXME: do we have an enum like class for py2.6? worth a dep?
class FetchMethods(object):
    SCM_URL = 'SCM_URL'
    LOCAL_FILE = 'LOCAL_FILE'
    REMOTE_URL = 'REMOTE_URL'
    GALAXY_URL = 'GALAXY_URL'


def choose_content_fetch_method(content_spec_string):
    log.debug('content_spec_string: %s', content_spec_string)

    if is_scm(content_spec_string):
        # create tar file from scm url
        return FetchMethods.SCM_URL

    comma_parts = content_spec_string.split(',', 1)
    potential_filename = comma_parts[0]
    if os.path.isfile(potential_filename):
        # installing a local tar.gz
        return FetchMethods.LOCAL_FILE

    if '://' in content_spec_string:
        return FetchMethods.REMOTE_URL

    # if it doesnt look like anything else, assume it's galaxy
    return FetchMethods.GALAXY_URL


def resolve(data):
    src = data['src']
    if data['name'] is None:
        scm_name = content_spec_parse.repo_url_to_repo_name(src)
        data['name'] = scm_name
        if '+' in src:
            (scm_url, scm_src) = src.split('+', 1)
            data['scm'] = scm_url
            data['src'] = scm_src

    # split the name on '.' and recombine the first 1 or 2
    name_parts = data['name'].split('.')
    new_name_parts = []
    new_name_parts.append(name_parts.pop(0))

    # we may not have a second part to the name
    try:
        new_name_parts.append(name_parts.pop(0))
    except IndexError:
        pass

    # combine the name parts, which may be one or two parts
    data['name'] = '.'.join(new_name_parts)

    return data


def spec_data_from_string(content_spec_string):
    fetch_method = choose_content_fetch_method(content_spec_string)

    log.debug('fetch_method: %s', fetch_method)

    spec_data = content_spec_parse.parse_string(content_spec_string)
    spec_data['fetch_method'] = fetch_method

    log.debug('spec_data: %s', spec_data)

    resolver = resolve
    if fetch_method == FetchMethods.GALAXY_URL:
        resolver = galaxy_content_spec.resolve

    resolved_name = resolver(spec_data)
    log.debug('resolved_name: %s', resolved_name)
    spec_data.update(resolved_name)

    return spec_data


def content_spec_from_string(content_spec_string):
    spec_data = spec_data_from_string(content_spec_string)

    return ContentSpec(**spec_data)
