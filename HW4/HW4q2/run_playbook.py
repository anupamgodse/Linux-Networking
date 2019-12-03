from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase

loader = DataLoader()
#inventory = Inventory(loader=loader, variable_manager=variable_manager,host_list='/home/felixc/ansible/hosts')

inventory = InventoryManager(loader=loader, sources=['./hosts'])

variable_manager = VariableManager(loader=loader, inventory=inventory)

vars = dict()
vars['c_name'] = 'test_C'

variable_manager.extra_vars['c_name']='test_c'

print(variable_manager.extra_vars)

passwords={}

Options = namedtuple('Options',['connection','remote_user','ask_sudo_pass','verbosity','ack_pass','module_path','forks','become','become_method','become_user','check','listhosts','listtasks','listtags','syntax','sudo_user','sudo','diff'])

options = Options(connection='smart',remote_user=None,ack_pass=None,sudo_user=None,forks=5,sudo=None,ask_sudo_pass=False,verbosity=5,module_path=None,become=None,become_method=None,become_user=None,check=False,diff=False,listhosts=None,listtasks=None,listtags=None,syntax=None)

playbook = PlaybookExecutor(playbooks=['playbooks/create-container.yml'],inventory=inventory,variable_manager=variable_manager,loader=loader,passwords=passwords)

tqm = None
try:
    tqm = TaskQueueManager(
              inventory=inventory,
              variable_manager=variable_manager,
              loader=loader,
              #options=options,
              passwords=passwords,
              #stdout_callback=results_callback,  # Use our custom callback instead of the ``default`` callback plugin
          )
    result = tqm.run(playbook)
finally:
    if tqm is not None:
        tqm.cleanup()
