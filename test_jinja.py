import jinja2.meta
env = jinja2.Environment()
ast = env.parse('{% raw %}${{ secrets.VAR }}{% endraw %}')
print(jinja2.meta.find_undeclared_variables(ast))
