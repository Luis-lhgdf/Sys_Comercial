lista = (1, 2, 3)

modulo = "Estoque"
submodulo = "ENTRADA"

info_user = [
    "luis",
    "ADM",
    [
        (
            1,
            "luis",
            "Estoque",
            "ENTRADA",
            "liberado",
            "bloqueado",
            "bloqueado",
            "bloqueado",
            1,
        ),
        (
            2,
            "luis",
            "Estoque",
            "SAIDA",
            "liberado",
            "liberado",
            "liberado",
            "liberado",
            1,
        ),
        (
            3,
            "luis",
            "Estoque",
            "INVENTARIO",
            "liberado",
            "liberado",
            "liberado",
            "liberado",
            1,
        ),
        (
            4,
            "luis",
            "Cadastro",
            "CAD ITEM",
            "liberado",
            "liberado",
            "liberado",
            "liberado",
            1,
        ),
        (
            5,
            "luis",
            "Cadastro",
            "CAD CLIENTE",
            "liberado",
            "liberado",
            "liberado",
            "liberado",
            1,
        ),
        (
            6,
            "luis",
            "Cadastro",
            "CAD USUARIO",
            "liberado",
            "liberado",
            "liberado",
            "liberado",
            1,
        ),
        (
            7,
            "luis",
            "Cadastro",
            "GERENCIAR USER",
            "liberado",
            "liberado",
            "liberado",
            "liberado",
            1,
        ),
        (
            8,
            "luis",
            "Agenda",
            "AGENDA",
            "liberado",
            "liberado",
            "liberado",
            "liberado",
            1,
        ),
        (
            9,
            "luis",
            "Carteira",
            "VENDAS",
            "liberado",
            "liberado",
            "liberado",
            "liberado",
            1,
        ),
        (
            10,
            "luis",
            "Carteira",
            "FATURAMENTO",
            "liberado",
            "liberado",
            "liberado",
            "liberado",
            1,
        ),
        (
            11,
            "luis",
            "Financas",
            "DESPESAS",
            "liberado",
            "liberado",
            "liberado",
            "liberado",
            1,
        ),
        (
            12,
            "luis",
            "Financas",
            "OUTRAS RENDAS",
            "liberado",
            "liberado",
            "liberado",
            "liberado",
            1,
        ),
        (
            13,
            "luis",
            "Usuario",
            "USUARIO",
            "liberado",
            "liberado",
            "liberado",
            "liberado",
            1,
        ),
        (
            14,
            "luis",
            "Configuracoes",
            "CONFIGURACOES",
            "liberado",
            "liberado",
            "liberado",
            "liberado",
            1,
        ),
    ],
]


def has_permission(user_info, module_name, selected_submodulo=None):
    for module_data in user_info[2]:
        if selected_submodulo is None:
            if module_data[2] == module_name:
                permissions = module_data[4:8]
                if all(perm == "bloqueado" for perm in permissions):
                    return False, []
                else:
                    return True, permissions
        else:
            if module_data[2] == module_name and module_data[3] == selected_submodulo:
                permissions = module_data[4:8]
                if all(perm == "bloqueado" for perm in permissions):
                    return False, []
                else:
                    return True, permissions
    return False, []


tem_acesso, permissoes = has_permission(info_user, modulo, submodulo)

if tem_acesso:
    print("Tem acesso. Permissões:", permissoes)
else:
    print("Não tem acesso")
