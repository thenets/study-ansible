# How to create and use a plugin

## Plugin

Documentation to set the Plugins path:
- https://docs.ansible.com/ansible/latest/reference_appendices/config.html#default-filter-plugin-path

METHOD 1:

Set environment variable.

```bash
# Set the env var with the plugins path
export ANSIBLE_FILTER_PLUGINS=$(pwd)/plugins

# Then run the playbook
ansible-playbook playbook.yml
```

METHOD 2:

Create the `ansible.cfg` with the plugins dir path.

```ini
[defaults]
filter_plugins = ./plugins
```
