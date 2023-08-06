import skale.utils.helper as Helper
from web3 import Web3, WebsocketProvider
import skale.contracts as contracts

class Skale:
  def __init__(self, ip, port, abi_filepath=None):
    ws_addr = Helper.generate_ws_addr(ip, port)
    self.web3 = Web3(WebsocketProvider(ws_addr))
    self.abi = Helper.get_abi(abi_filepath)
    self.__contracts = {}
    self.__init_contracts()

  def __init_contracts(self):
    self.add_lib_contract('manager', contracts.NodeManager)
    self.add_lib_contract('token', contracts.Token)

    self.add_lib_contract('nodes', contracts.BaseContract)
    self.add_lib_contract('groups', contracts.BaseContract)
    self.add_lib_contract('validators', contracts.BaseContract)
    self.add_lib_contract('schains', contracts.BaseContract)

  def add_lib_contract(self, name, contract_class):
    address = self.abi[f'skale_{name}_address']
    abi = self.abi[f'skale_{name}_abi']

    self.add_contract(name, contract_class(self, name, address, abi))

  def add_contract(self, name, skale_contract):
    self.__contracts[name] = skale_contract

  def get_contract_by_name(self, name):
    return self.__contracts[name]

  def __getattr__(self, name):
    if name not in self.__contracts:
      raise AttributeError(name)
    return self.get_contract_by_name(name)
