#son-workspace

Create workspaces and projects

This tool is responsible to create workspaces and generate project layouts.

```sh
usage: son-workspace [-h] [--init] [--workspace WORKSPACE] [--project PROJECT]
                     [--debug]

Generate new sonata workspaces and project layouts

optional arguments:
  -h, --help            show this help message and exit
  
  --init                Create a new sonata workspace
  
  --workspace WORKSPACE
                        location of existing (or new) workspace. If not
                        specified will assume '$HOME/.son-workspace'
                        
  --project PROJECT     create a new project at the specified location
  
  --debug               increases logging level to debug
```

Example on how to create an workspace and a project:

```sh
	son-workspace --init --workspace /home/user/workspaces/ws1
	son-workspace --workspace /home/user/workspace/ws1 --project /home/user/workspace/ws1/projects/p1
```

This example creates the workspace 'ws1' and a project 'p1' associated with it.

