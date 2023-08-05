import os
import os.path
import subprocess
import shlex
import errno

from cis_client.lib.cis_north import access_key_client
from cis_client import exception


def aspera_upload(north_host, ingest_point, path, destination_path=None, max_transfer_rate='1G', **kwargs):
    """Aspera upload"""

    if destination_path is None:
        destination_path = os.path.basename(path)
    destination_path = destination_path.lstrip('/')

    ingest_point_info, access_key = access_key_client.get_access_key(north_host, ingest_point, **kwargs)

    # 'ASPERA_SCP_PASS=<access-key> ascp -P 33001 --user=<UDN-username>
    #   --host=b.aspera.cdx-dev.dataingest.net --mode=send <local-path> <dest-path>'
    aspera_template = ingest_point_info['gateway']['protocols']['aspera']['template']
    aspera_cmd = aspera_template.replace('<dest-path>', destination_path, 1).\
                                 replace('<local-path>', path, 1). \
                                 replace('<UDN-username>', kwargs['username'], 1). \
                                 replace('<access-key>', access_key, 1)
    aspera_cmd_args = shlex.split(aspera_cmd)
    aspera_cmd_args_resume = [aspera_cmd_args[1], '-k2', '-l{}'.format(max_transfer_rate), '-d']
    aspera_cmd_args_resume.extend(aspera_cmd_args[2:])
    try:
        ret = subprocess.call(aspera_cmd_args_resume, env=dict(os.environ, **{'ASPERA_SCP_PASS': access_key}))
    except OSError as e:
        if e.errno == errno.ENOENT:
            raise exception.AsperaExecutableNotFound()
        raise
    if int(ret) != 0:
        raise exception.AsperaUploadFailed(ret)
