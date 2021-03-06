#
# Copyright (c) 2014 Juniper Networks, Inc. All rights reserved.
#

from vnc_api import exceptions as vnc_exc
try:
    from neutron.common.exceptions import BadRequest
except ImportError:
    from neutron_lib.exceptions import BadRequest

from neutron_lbaas.extensions.loadbalancerv2 import LoadBalancerPluginBaseV2

from neutron_plugin_contrail.common import utils
from neutron_plugin_contrail.plugins.opencontrail.loadbalancer.v2 import loadbalancer_healthmonitor
from neutron_plugin_contrail.plugins.opencontrail.loadbalancer.v2 import loadbalancer_member
from neutron_plugin_contrail.plugins.opencontrail.loadbalancer.v2 import loadbalancer_pool
from neutron_plugin_contrail.plugins.opencontrail.loadbalancer.v2 import loadbalancer
from neutron_plugin_contrail.plugins.opencontrail.loadbalancer.v2 import listener


class LoadBalancerPluginDbV2(LoadBalancerPluginBaseV2):
    @property
    def api(self):
        if hasattr(self, '_api'):
            return self._api

        self._api = utils.get_vnc_api_instance()

        return self._api

    @property
    def pool_manager(self):
        if hasattr(self, '_pool_manager'):
            return self._pool_manager

        self._pool_manager = \
            loadbalancer_pool.LoadbalancerPoolManager(self.api)

        return self._pool_manager

    @property
    def loadbalancer_manager(self):
        if hasattr(self, '_loadbalancer_manager'):
            return self._loadbalancer_manager

        self._loadbalancer_manager = loadbalancer.LoadbalancerManager(self.api)

        return self._loadbalancer_manager

    @property
    def listener_manager(self):
        if hasattr(self, '_listener_manager'):
            return self._listener_manager
        self._listener_manager = listener.ListenerManager(self.api)

        return self._listener_manager

    @property
    def member_manager(self):
        if hasattr(self, '_member_manager'):
            return self._member_manager

        self._member_manager = \
            loadbalancer_member.LoadbalancerMemberManager(self.api)

        return self._member_manager

    @property
    def monitor_manager(self):
        if hasattr(self, '_monitor_manager'):
            return self._monitor_manager
        self._monitor_manager = \
            loadbalancer_healthmonitor.LoadbalancerHealthmonitorManager(
                self.api)

        return self._monitor_manager

    def get_api_client(self):
        return self.api

    def get_loadbalancers(self, context, filters=None, fields=None):
        self.api.set_auth_token(context.auth_token)
        return self.loadbalancer_manager.get_collection(context, filters, fields)

    def get_loadbalancer(self, context, id, fields=None):
        self.api.set_auth_token(context.auth_token)
        return self.loadbalancer_manager.get_resource(context, id, fields)

    def create_loadbalancer(self, context, loadbalancer):
        self.api.set_auth_token(context.auth_token)
        try:
            return self.loadbalancer_manager.create(context, loadbalancer)
        except vnc_exc.PermissionDenied as ex:
            raise BadRequest(resource='loadbalancer', msg=str(ex))

    def update_loadbalancer(self, context, id, loadbalancer):
        self.api.set_auth_token(context.auth_token)
        return self.loadbalancer_manager.update(context, id, loadbalancer)

    def delete_loadbalancer(self, context, id):
        self.api.set_auth_token(context.auth_token)
        return self.loadbalancer_manager.delete(context, id)

    def create_listener(self, context, listener):
        self.api.set_auth_token(context.auth_token)
        try:
            return self.listener_manager.create(context, listener)
        except vnc_exc.PermissionDenied as ex:
            raise BadRequest(resource='listener', msg=str(ex))

    def get_listener(self, context, id, fields=None):
        self.api.set_auth_token(context.auth_token)
        return self.listener_manager.get_resource(context, id, fields)

    def get_listeners(self, context, filters=None, fields=None):
        self.api.set_auth_token(context.auth_token)
        return self.listener_manager.get_collection(context, filters, fields)

    def update_listener(self, context, id, listener):
        self.api.set_auth_token(context.auth_token)
        return self.listener_manager.update(context, id, listener)

    def delete_listener(self, context, id):
        self.api.set_auth_token(context.auth_token)
        return self.listener_manager.delete(context, id)

    def get_pools(self, context, filters=None, fields=None):
        self.api.set_auth_token(context.auth_token)
        return self.pool_manager.get_collection(context, filters, fields)

    def get_pool(self, context, id, fields=None):
        self.api.set_auth_token(context.auth_token)
        return self.pool_manager.get_resource(context, id, fields)

    def create_pool(self, context, pool):
        self.api.set_auth_token(context.auth_token)
        try:
            return self.pool_manager.create(context, pool)
        except vnc_exc.PermissionDenied as ex:
            raise BadRequest(resource='pool', msg=str(ex))

    def update_pool(self, context, id, pool):
        self.api.set_auth_token(context.auth_token)
        return self.pool_manager.update(context, id, pool)

    def delete_pool(self, context, id):
        self.api.set_auth_token(context.auth_token)
        return self.pool_manager.delete(context, id)

    def get_pool_members(self, context, pool_id, filters=None, fields=None):
        self.api.set_auth_token(context.auth_token)
        return self.member_manager.get_collection(context, pool_id, filters, fields)

    def get_pool_member(self, context, id, pool_id, fields=None):
        self.api.set_auth_token(context.auth_token)
        return self.member_manager.get_resource(context, id, pool_id, fields)

    def create_pool_member(self, context, pool_id, member):
        self.api.set_auth_token(context.auth_token)
        try:
            return self.member_manager.create(context, pool_id, member)
        except vnc_exc.PermissionDenied as ex:
            raise BadRequest(resource='member', msg=str(ex))

    def update_pool_member(self, context, id, pool_id, member):
        self.api.set_auth_token(context.auth_token)
        return self.member_manager.update(context, id, member)

    def delete_pool_member(self, context, id, pool_id):
        self.api.set_auth_token(context.auth_token)
        return self.member_manager.delete(context, id, pool_id)

    def get_members(self, context, filters=None, fields=None):
        pass

    def get_member(self, context, id, fields=None):
        pass

    def get_healthmonitors(self, context, filters=None, fields=None):
        self.api.set_auth_token(context.auth_token)
        return self.monitor_manager.get_collection(context, filters, fields)

    def get_healthmonitor(self, context, id, fields=None):
        self.api.set_auth_token(context.auth_token)
        return self.monitor_manager.get_resource(context, id, fields)

    def create_healthmonitor(self, context, healthmonitor):
        self.api.set_auth_token(context.auth_token)
        try:
            return self.monitor_manager.create(context, healthmonitor)
        except vnc_exc.PermissionDenied as ex:
            raise BadRequest(resource='healthmonitor', msg=str(ex))

    def update_healthmonitor(self, context, id, healthmonitor):
        self.api.set_auth_token(context.auth_token)
        return self.monitor_manager.update(context, id, healthmonitor)

    def delete_healthmonitor(self, context, id):
        self.api.set_auth_token(context.auth_token)
        return self.monitor_manager.delete(context, id)

    def stats(self, context, loadbalancer_id):
        pass

    def statuses(self, context, loadbalancer_id):
        pass

    def get_l7policies(self, context, filters=None, fields=None):
        pass

    def get_l7policy(self, context, id, fields=None):
        pass

    def create_l7policy(self, context, l7policy):
        pass

    def update_l7policy(self, context, id, l7policy):
        pass

    def delete_l7policy(self, context, id):
        pass

    def get_l7policy_rules(self, context, l7policy_id,
                           filters=None, fields=None):
        pass

    def get_l7policy_rule(self, context, id, l7policy_id, fields=None):
        pass

    def create_l7policy_rule(self, context, rule, l7policy_id):
        pass

    def update_l7policy_rule(self, context, id, rule, l7policy_id):
        pass

    def delete_l7policy_rule(self, context, id, l7policy_id):
        pass

    def create_graph(self, context, graph):
        pass
