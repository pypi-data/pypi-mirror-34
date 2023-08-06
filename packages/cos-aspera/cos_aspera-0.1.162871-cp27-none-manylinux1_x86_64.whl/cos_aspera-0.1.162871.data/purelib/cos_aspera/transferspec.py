import json

class TransferSpecEncoder(json.JSONEncoder):
    def default(self, o):
        return {k.lstrip('_'): v for k, v in vars(o).items() if v is not None}

class NodeError(object):
    def __init__(self):
        self._code = None
        self._reason = None
        self._user_message = None
        self._internal_message = None
        self._internal_info = None

    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.code must be an int')
        self._code = value

    @property
    def reason(self):
        return self._reason
    @reason.setter
    def reason(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.reason must be an str')
        self._reason = value

    @property
    def user_message(self):
        return self._user_message
    @user_message.setter
    def user_message(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.user_message must be an str')
        self._user_message = value

    @property
    def internal_message(self):
        return self._internal_message
    @internal_message.setter
    def internal_message(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.internal_message must be an str')
        self._internal_message = value

    @property
    def internal_info(self):
        return self._internal_info
    @internal_info.setter
    def internal_info(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.internal_info must be an str')
        self._internal_info = value

    def toJson(self):
        return json.dumps(self, cls=TransferSpecEncoder)

#--------------------------------------

class NodePath(object):
    def __init__(self):
        self._destination = None
        self._path = None
        self._source = None
        self._storage_root = None
        self._type = None
        self._error = None

    @property
    def destination(self):
        return self._destination
    @destination.setter
    def destination(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.destination must be an str')
        self._destination = value

    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.path must be an str')
        self._path = value

    @property
    def source(self):
        return self._source
    @source.setter
    def source(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.source must be an str')
        self._source = value

    @property
    def storage_root(self):
        return self._storage_root
    @storage_root.setter
    def storage_root(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.storage_root must be an str')
        self._storage_root = value

    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.type must be an str')
        self._type = value

    ##
    # The error response object.
    #
    @property
    def error(self):
        return self._error
    @error.setter
    def error(self, value):
        if not isinstance(value, NodeError):
            raise TypeError('TransferSpec.error must be an NodeError')
        self._error = value

    def toJson(self):
        return json.dumps(self, cls=TransferSpecEncoder)
#----------------------------------------
class TransferSpec(object):
    def __init__(self):
        self._remote_host = None
        self._direction = None
        self._remote_user = None
        self._authentication = None
        self._remote_password = None
        self._ssh_port = None
        self._fasp_port = None
        self._http_fallback = None
        self._http_fallback_port = None
        self._create_dir = None
        self._destination_root = None
        self._rate_policy = None
        self._target_rate_kbps = None
        self._min_rate_kbps = None
        self._lock_rate_policy = None
        self._target_rate_cap_kbps = None
        self._lock_target_rate = None
        self._lock_min_rate = None
        self._resume = None
        self._cookie = None
        self._dgram_size = None
        self._content_protection = None
        self._content_protection_passphrase = None
        self._cipher = None
        self._multi_session = None
        self._multi_session_threshold = None
        self._client_access_key = None
        self._client_cluster_id = None
        self._client_token_user_id = None
        self._delete_source = None
        self._destination_root_id = None
        self._endpoint = None
        self._error = None
        self._keepalive = None
        self._https_key_filename = None
        self._https_certificate_filename = None
        self._https_proxy = None
        self._ignore_host_key = None
        self._save_before_override = None
        self._partial_file_suffix = None
        self._report_skipped_files = None
        self._auto_bwidth_discovery = None
        self._file_checksum = None #none, md5, sha1, sha256, sha384, sha512
        self._rexmsg_size = None
        self._exclude_newer_than = None
        self._exclude_older_than = None
        self._overwrite_policy = None
        self._paths = None
        self._preserve_times = None
        self._proxy = None
        self._rate_policy_allowed = None
        self._remote_access_key = None
        self._resume_policy = None
        self._server_access_key = None
        self._server_cluster_id = None
        self._server_token_user_id = None
        self._source_root = None
        self._source_root_id = None
        self._sshfp = None
        self._tags = None
        self._token = None
        self._min_rate_cap_kbps = None
        self._target_rate_percentage = None
        self._vlink_id = None


    ##
     # The fully qualified domain name or IP address of the transfer server.
     #    
    @property
    def remote_host(self):
        return self._remote_host
    @remote_host.setter
    def remote_host(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.remote_host must be an str')
        self._remote_host = value

    ##
     # Transfer direction. Possible values:
     # send, receive
     #
    @property
    def direction(self):
        return self._direction
    @direction.setter
    def direction(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.direction must be an str')
        self._direction = value

    ##
     # The username to use for authentication. 
     # For password authentication.
     #
    @property
    def remote_user(self):
        return self._remote_user
    @remote_user.setter
    def remote_user(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.remote_user must be an str')
        self._remote_user = value

    @property
    ##
     # The algorithm used to encrypt data sent during a transfer. Use this option when transmitting sensitive data. Increases CPU utilization.
     # Possible values:
     # aes128, aes192, aes256
     #
    def authentication(self):
        return self._authentication
    @authentication.setter
    def authentication(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.authentication must be an str')
        self._authentication = value

    @property
    ##
     # The password to use when authentication is set to "password".
     #
    def remote_password(self):
        return self._remote_password
    @remote_password.setter
    def remote_password(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.remote_password must be an str')
        self._remote_password = value

    ##
     # The server's TCP port that is listening for SSH connections.
     # FASP initiates transfers through SSH. Default is 33001
     #
    @property
    def ssh_port(self):
        return self._ssh_port
    @ssh_port.setter
    def ssh_port(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.ssh_port must be an int')
        self._ssh_port = value

    ##
     # The UDP port for FASP to use. The default value is satisfactory for most situations.
     # However, it can be changed to satisfy firewall requirements. The default is 33001.
     #
    @property
    def fasp_port(self):
        return self._fasp_port
    @fasp_port.setter
    def fasp_port(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.fasp_port must be an int')
        self._fasp_port = value

    ##
     # Attempts to perform an HTTP transfer if a FASP transfer cannot be performed.
     #
    @property
    def http_fallback(self):
        return self._http_fallback
    @http_fallback.setter
    def http_fallback(self, value):
        if not isinstance(value, bool):
            raise TypeError('TransferSpec.http_fallback must be an bool')
        self._http_fallback = value
    
    ##
     # The port where the Aspera HTTP server is servicing HTTP transfers.
     # Defaults to port 443 if a cipher is enabled, otherwise port 80.
     #
    @property
    def http_fallback_port(self):
        return self._http_fallback_port
    @http_fallback_port.setter
    def http_fallback_port(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.http_fallback_port must be an int')
        self._http_fallback_port = value

    @property
    def create_dir(self):
        return self._create_dir
    @create_dir.setter
    def create_dir(self, value):
        if not isinstance(value, bool):
            raise TypeError('TransferSpec.create_dir must be an bool')
        self._create_dir = value

    ##
     # The transfer destination file path. If destinations are specified in paths, this value is prepended to each destination.
     #
    @property
    def destination_root(self):
        return self._destination_root
    @destination_root.setter
    def destination_root(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.destination_root must be an str')
        self._destination_root = value

    ##
     # The congestion control behavior to use when sharing bandwidth.
     # Allowed values:
     # high: When sharing bandwidth, transfer at twice the rate of a transfer using a fair policy.
     # fair (default value): Share bandwidth equally with other traffic.
     # low: Use only un-utilized bandwidth.
     # fixed: Transfer at the target rate, regardless of the actual network capacity.
     # Do not share bandwidth. The fixed policy can decrease transfer performance and cause problems on the target storage.
     #
    @property
    def rate_policy(self):
        return self._rate_policy
    @rate_policy.setter
    def rate_policy(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.rate_policy must be an str')
        self._rate_policy = value

    ##
     # The desired speed of the transfer. If there is competing network traffic, FASP may share this bandwidth, depending on the rate_policy.
     # By default, server-side target rate settings will be used. Will respect both local- and server-side target rate caps if set.
     #
    @property
    def target_rate_kbps(self):
        return self._target_rate_kbps
    @target_rate_kbps.setter
    def target_rate_kbps(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.target_rate_kbps must be an int')
        self._target_rate_kbps = value

    ##
    # The minimum transfer rate, in Kbps.
    #   
    @property
    def min_rate_kbps(self):
        return self._min_rate_kbps
    @min_rate_kbps.setter
    def min_rate_kbps(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.min_rate_kbps must be an int')
        self._min_rate_kbps = value

    ##
     # Prevents the user from changing the rate policy during a transfer.
     #
    @property
    def lock_rate_policy(self):
        return self._lock_rate_policy
    @lock_rate_policy.setter
    def lock_rate_policy(self, value):
        if not isinstance(value, bool):
            raise TypeError('TransferSpec.lock_rate_policy must be an bool')
        self._lock_rate_policy = value

    ##
     # Limit the transfer rate that the user can adjust the target and minimum rates to.
     #
    @property
    def target_rate_cap_kbps(self):
        return self._target_rate_cap_kbps
    @target_rate_cap_kbps.setter
    def target_rate_cap_kbps(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.target_rate_cap_kbps must be an int')
        self._target_rate_cap_kbps = value

    ##
     # Prevents the user from changing the target rate during a transfer.
     #
    @property
    def lock_target_rate(self):
        return self._lock_target_rate
    @lock_target_rate.setter
    def lock_target_rate(self, value):
        if not isinstance(value, bool):
            raise TypeError('TransferSpec.lock_target_rate must be an bool')
        self._lock_target_rate = value

    ##
     # Prevents the user from changing the minimum rate during a transfer.
     #
    @property
    def lock_min_rate(self):
        return self._lock_min_rate
    @lock_min_rate.setter
    def lock_min_rate(self, value):
        if not isinstance(value, bool):
            raise TypeError('TransferSpec.lock_min_rate must be an bool')
        self._lock_min_rate = value

    @property
    def resume(self):
        return self._resume
    @resume.setter
    def resume(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.resume must be an str')
        self._resume = value

    ##
     # Data to associate with the transfer. The cookie is reported to both client- and server-side applications monitoring FASP transfers.
     # It is often used by applications to identify associated transfers.
     #
    @property
    def cookie(self):
        return self._cookie
    @cookie.setter
    def cookie(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.cookie must be an str')
        self._cookie = value

    ##
     # The IP datagram size for FASP to use. If this value is not specified, FASP will automatically detects and use the path MTU as the datagram size.
     # Use this option only to satisfy networks with strict MTU requirements.
     #
    @property
    def dgram_size(self):
        return self._dgram_size
    @dgram_size.setter
    def dgram_size(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.dgram_size must be an int')
        self._dgram_size = value

    @property
    ##
     # Enables content protection (encryption-at-rest), which keeps files encrypted on the server.
     # Encrypted files have the extension ".aspera-env".
     # Possible values: decrypt, encrypt, disabled
     #
    def content_protection(self):
        return self._content_protection
    @content_protection.setter
    def content_protection(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.content_protection must be an str')
        self._content_protection = value

    ##
     # A passphrase used to encrypt or decrypt files.
     #
    @property
    def content_protection_passphrase(self):
        return self._content_protection_passphrase
    @content_protection_passphrase.setter
    def content_protection_passphrase(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.content_protection_passphrase must be an str')
        self._content_protection_passphrase = value

    @property
    def cipher(self):
        return self._content_protection_passphrase
    @cipher.setter
    def cipher(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.cipher must be an str')
        self._cipher = value

    @property
    def multi_session(self):
        return self._multi_session
    @multi_session.setter
    def multi_session(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.multi_session must be an int')
        self._multi_session = value
   ##
   #  set threshold for  files that will be considered for multiple sessions.
   #
    @property
    def multi_session_threshold(self):
        return self._multi_session_threshold   
    @multi_session_threshold.setter
    def multi_session_threshold(self, value):
        if not isinstance(value, long):
            raise TypeError('TransferSpec.multi_session_threshold must be a long')
        self._multi_session_threshold = value
    ##
    # The access key ID of the access key that is provided by the client, if any.
    #
    @property
    def client_access_key(self):
        return self._client_access_key
    @client_access_key.setter
    def client_access_key(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.client_access_key must be an str')
        self._client_access_key = value

    @property
    def client_cluster_id(self):
        return self._client_cluster_id
    @client_cluster_id.setter
    def client_cluster_id(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.client_cluster_id must be an str')
        self._client_cluster_id = value

    @property
    def client_token_user_id(self): 
        return self._client_token_user_id
    @client_token_user_id.setter
    def client_token_user_id(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.client_token_user_id must be an str')
        self._client_token_user_id = value

    ##
    # Delete the source if all source files, empty directories and the source argument itself are removed after they are successfully transferred.
    # Default: false.
    #
    @property
    def delete_source(self):
        return self._delete_source
    @delete_source.setter
    def delete_source(self, value):
        if not isinstance(value, bool):
            raise TypeError('TransferSpec.delete_source must be an bool')
        self._delete_source = value
    ##
    # The file ID of the destination root directory. Required when using Bearer token auth for the destination node.
    #
    @property
    def destination_root_id(self):
        return self._destination_root_id
    @destination_root_id.setter
    def destination_root_id(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.destination_root_id must be an str')
        self._destination_root_id = value

    ##
    # The authentication endpoint; required for Amazon S3 and IBM COS S3.
    #
    @property
    def endpoint(self):
        return self._endpoint
    @endpoint.setter
    def endpoint(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.endpoint must be an str')
        self._endpoint = value

    @property
    def error(self):
        return self._error
    @error.setter
    def error(self, value):
        if not isinstance(value, NodeError):
            raise TypeError('TransferSpec.error must be an NodeError')
        self._error = value
    ##
    # If true, transfer in persistent mode.
    #
    @property
    def keepalive(self):
        return self._keepalive
    @keepalive.setter
    def keepalive(self, value):
        if not isinstance(value, bool):
            raise TypeError('TransferSpec.keepalive must be an bool')
        self._keepalive = value

    @property
    def https_key_filename(self):
        return self._https_key_filename
    @https_key_filename.setter
    def https_key_filename(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.https_key_filename must be an str')
        self._https_key_filename = value

    @property
    def https_certificate_filename(self):
        return self._https_certificate_filename
    @https_certificate_filename.setter
    def https_certificate_filename(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.https_certificate_filename must be an str')
        self._https_certificate_filename = value

    @property
    def https_proxy(self):
        return self._https_proxy
    @https_proxy.setter
    def https_proxy(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.https_proxy must be an str')
        self._https_proxy = value

    @property
    def ignore_host_key(self):
        return self._ignore_host_key
    @ignore_host_key.setter
    def ignore_host_key(self, value):
        if not isinstance(value, bool):
            raise TypeError('TransferSpec.ignore_host_key must be an bool')
        self._ignore_host_key = value

    @property
    def save_before_override(self):
        return self._save_before_override
    @save_before_override.setter
    def save_before_override(self, value):
        if not isinstance(value, bool):
            raise TypeError('TransferSpec.save_before_override must be an bool')
        self._save_before_override = value

    @property
    def partial_file_suffix(self):
        return self._partial_file_suffix
    @partial_file_suffix.setter
    def partial_file_suffix(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.partial_file_suffix must be an str')
        self._partial_file_suffix = value

    @property
    def report_skipped_files(self):
        return self._report_skipped_files
    @report_skipped_files.setter
    def report_skipped_files(self, value):
        if not isinstance(value, bool):
            raise TypeError('TransferSpec.report_skipped_files must be an bool')
        self._report_skipped_files = value

    @property
    def auto_bwidth_discovery(self):
        return self._auto_bwidth_discovery
    @auto_bwidth_discovery.setter
    def auto_bwidth_discovery(self, value):
        if not isinstance(value, bool):
            raise TypeError('TransferSpec.auto_bwidth_discovery must be an bool')
        self._auto_bwidth_discovery = value

    ##
     # File checksum. Possible values:
     # none, md5, sha1, sha256, sha384, sha512
     #
    @property
    def file_checksum(self):
        return self._file_checksum
    @file_checksum.setter
    def file_checksum(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.file_checksum must be an str')
        self._file_checksum = value

    @property
    def rexmsg_size(self):
        return self._rexmsg_size
    @rexmsg_size.setter
    def rexmsg_size(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.rexmsg_size must be an int')
        self._rexmsg_size = value

    ##
    # Exclude files, but not directories, from the transfer if they are newer than the specified time.
    # Time is specified as number of seconds after the source computer's epoch.
    #
    @property
    def exclude_newer_than(self):
        return self._exclude_newer_than
    @exclude_newer_than.setter
    def exclude_newer_than(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.exclude_newer_than must be an int')
        self._exclude_newer_than = value

    ## 
     # Excludes files from the transfer based on when the file was last changed.
     # This positive value is compared to the "mtime" timestamp in the source file system, usually seconds
     # since 1970-01-01 00:00:00.
     #
    @property
    def exclude_older_than(self):
        return self._exclude_older_than
    @exclude_older_than.setter
    def exclude_older_than(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.exclude_older_than must be an int')
        self._exclude_older_than = value

    @property
    def overwrite_policy(self):
        return self._overwrite_policy
    @overwrite_policy.setter
    def overwrite_policy(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.overwrite_policy must be an str')
        self._overwrite_policy = value

    ##
     # A list of the file and directory paths to transfer. 
     #
    @property
    def paths(self):
        return self._paths
    @paths.setter
    def paths(self, value):
        if not isinstance(value, list) and not all(isinstance(n, NodePath) for n in value):
            raise TypeError('TransferSpec.paths must be an NodePath list')
        self._paths = value

    ##
    # Preserve file timestamps.
    # Default: false.
    #
    @property
    def preserve_times(self):
        return self._preserve_times
    @preserve_times.setter
    def preserve_times(self, value):
        if not isinstance(value, bool):
            raise TypeError('TransferSpec.preserve_times must be an bool')
        self._preserve_times = value

    ##
    # The URL of the proxy server.
    #
    @property
    def proxy(self):
        return self._proxy
    @proxy.setter
    def proxy(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.proxy must be an str')
        self._proxy = value

    ##
    # The most aggressive rate policy that is allowed for the transfer. See rate_policy for values.
    #
    @property
    def rate_policy_allowed(self):
        return self._rate_policy_allowed
    @rate_policy_allowed.setter
    def rate_policy_allowed(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.rate_policy_allowed must be an str')
        self._rate_policy_allowed = value

    ##
    # Remote access key for the transfer.
    #
    @property
    def remote_access_key(self):
        return self._remote_access_key
    @remote_access_key.setter
    def remote_access_key(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.remote_access_key must be an str')
        self._remote_access_key = value

    @property
    def esume_policy(self):
        return self._esume_policy
    @esume_policy.setter
    def esume_policy(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.esume_policy must be an str')
        self._esume_policy = value

    ##
    # The access key ID of the access key that is provided to the remote node, if any.
    #
    @property
    def server_access_key(self):
        return self._server_access_key
    @server_access_key.setter
    def server_access_key(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.server_access_key must be an str')
        self._server_access_key = value

    @property
    def server_cluster_id(self):
        return self._server_cluster_id
    @server_cluster_id.setter
    def server_cluster_id(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.server_cluster_id must be an str')
        self._server_cluster_id = value

    ##
    # If the remote node provides a token, the username associated with the token.
    #
    @property
    def server_token_user_id(self):
        return self._server_token_user_id
    @server_token_user_id.setter
    def server_token_user_id(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.server_token_user_id must be an str')
        self._server_token_user_id = value

    ##
    # The source root directory of the files.
    #
    @property
    def source_root(self):
        return self._source_root
    @source_root.setter
    def source_root(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.source_root must be an str')
        self._source_root = value

    ##
    # The file ID of the source root directory. Required when using Bearer token auth for the source node.
    #
    @property
    def source_root_id(self):
        return self._source_root_id
    @source_root_id.setter
    def source_root_id(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.source_root_id must be an str')
        self._source_root_id = value

    ##
    # The node's SSH fingerprint, if it is configured in the node's aspera.conf.
    #
    @property
    def sshfp(self):
        return self._sshfp
    @sshfp.setter
    def sshfp(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.sshfp must be an str')
        self._sshfp = value

    # @property
    # def tags(self):
    #     return self._tags
    # @tags.setter
    # def tags(self, value):
    #     if not isinstance(value, Tags):
    #         raise TypeError('TransferSpec.tags must be an Tags')
    #     self._tags = value

    ##
     # Used for token-based authorization, which involves the server-side application generating a token
     # that gives the client rights to transfer a predetermined set of files.
     #
    @property
    def token(self):
        return self._token
    @token.setter
    def token(self, value):
        if not isinstance(value, str):
            raise TypeError('TransferSpec.token must be an str')
        self._token = value

    @property
    def min_rate_cap_kbps(self):
        return self._min_rate_cap_kbps
    @min_rate_cap_kbps.setter
    def min_rate_cap_kbps(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.min_rate_cap_kbps must be an int')
        self._min_rate_cap_kbps = value

    @property
    def target_rate_percentage(self):
        return self._target_rate_percentage
    @target_rate_percentage.setter
    def target_rate_percentage(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.target_rate_percentage must be an int')
        self._target_rate_percentage = value

    ##
    # The ID of the virtual link (bandwidth control) that is applied to the transfer.
    #
    @property
    def vlink_id(self):
        return self._vlink_id
    @vlink_id.setter
    def vlink_id(self, value):
        if not isinstance(value, int):
            raise TypeError('TransferSpec.vlink_id must be an int')
        self._vlink_id = value

    def toJson(self):
        return json.dumps(self, cls=TransferSpecEncoder)
