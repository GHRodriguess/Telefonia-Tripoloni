from dotenv import load_dotenv
import os
from ldap3  import Server, NTLM, core, Connection, ALL, SUBTREE 


load_dotenv()

class Conexão_AD():
    def __init__(self, username=None, password=None):
        if username and password:
            self.username = username
            self.password = password
        else:
            self.username = os.getenv("NOME_USUARIO_AD")
            self.password = os.getenv("SENHA_AD")
        self.servidor_ad = os.getenv("SERVIDOR_AD")
        self.dominio = os.getenv("SERVIDOR_AD")    
        self.base_dn = os.getenv("BASE_DN")

    def conecta_ad(self):        
        usuario_ad = f'{self.dominio}\\{self.username}'        
        servidor = Server(self.servidor_ad, get_info=ALL)        
        self.conexao = Connection(servidor, user=usuario_ad, password=self.password, authentication=NTLM, auto_bind=True)
        
    def desconecta_ad(self):
        self.conexao.unbind()
    
    def autenticar_usuario_ad(self):        
        try:             
            self.conecta_ad()            
            self.desconecta_ad()   
            return True
        except core.exceptions.LDAPBindError:
            return False
        except Exception as e:
            print(e)
            return False
    
    def get_info_user(self, user_search=None):
        user_search = self.username if user_search == None else user_search        
        filtro = f'(sAMAccountName={user_search})'
        atributos = ['displayName', 'mail', 'givenName', 'sn', 'memberOf', 'distinguishedName', 'title']
        self.conecta_ad()
        self.conexao.search(search_base=self.base_dn, search_filter=filtro, search_scope=SUBTREE, attributes=atributos)
        if self.conexao.entries:
            dados_usuario = self.conexao.entries[0]
            self.desconecta_ad()       
            dn = dados_usuario.distinguishedName.value
            partes = dn.split(",")
            setor = None     

            for i, parte in enumerate(partes):
                if parte.strip().startswith("OU="):
                    setor = parte.replace("OU=", "")
                    if partes[i+1].strip().startswith("OU="):
                        obra = f"{partes[i+1].replace('OU=', '')}"
                        break  
            
            #dados_usuario.title.value = cargo do usuário
            return {
                'nome_completo': dados_usuario.displayName.value,
                'email': dados_usuario.mail.value,
                'nome': dados_usuario.givenName.value,
                'sobrenome': dados_usuario.sn.value,
                'grupos': dados_usuario.memberOf.values,
                'setor': setor,
                'obra': obra,
            } 
        else:
            return None    

    def get_all_users(self, filter_user):
        if filter_user == "active":
            filtro = '(&(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))'
        elif filter_user == "inactive":
            filtro = '(&(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=2))' 
            
        atributos = ['sAMAccountName']
        self.conecta_ad()
    
        self.conexao.search(
            search_base=self.base_dn,
            search_filter=filtro,
            search_scope=SUBTREE,
            attributes=atributos
        )
        ignore_values = ["$"]
        usuarios = []
        for entry in self.conexao.entries:
            if any(ignore_value in entry.sAMAccountName.value for  ignore_value in ignore_values): 
                continue
            usuarios.append(entry.sAMAccountName.value)
            
        return usuarios