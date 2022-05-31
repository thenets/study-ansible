# How to use a script and parse the output

## Script

You can run the script by executing the following command:

```yaml
- name: Run a Python script
    ansible.builtin.script:
    executable: python3
    cmd: game-list.py
    register: game_list_raw_output
```

If your script returns a JSON object, you can use the `from_json` filter to
parse the output:

```yaml
- name: Convert output to JSON
    ansible.builtin.set_fact:
    game_list: "{{ game_list_raw_output.stdout | from_json }}"

- name: Debug game list
    ansible.builtin.debug:
    var: game_list
```
