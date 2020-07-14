# Beautified Conan Info DOT Template

Since [Conan 1.27](https://docs.conan.io/en/1.26/index.html), it is now possible to customize the `conan info` output command by means of [Jinja2 Templates](https://docs.conan.io/en/latest/extending/template_system/info_graph.html).

This repository contains the concept proposed in this [original contribution proposal](https://github.com/conan-io/conan/pull/6815) based on the template-based info feature.


## Installation

To install the template just type

```bash
conan config install https://github.com/alacasta/beautified-conan-info-dot-template.git -sf templates/output/ -tf templates/output/
```

From that moment, the template is install and the output commands for

```bash
conan info . --graph=graph_filename.dot
```

will be based on this template.

To uninstall it, just navigate to `conan_cache/templates/output/` and remove `info_graph.dot` file.

## How to use it

It is just required to run `conan info` command in any of the [many available ways](https://docs.conan.io/en/latest/reference/commands/consumer/info.html) and then if needed, transform it to some embeddable format using [Graphviz DOT](https://www.graphviz.org/pdf/dotguide.pdf).

For example, to export it to PNG

```bash
dot graph_filename.dot -Tpng > graph_in_png_filename.png
```

## Example

In `example/conanfile.py` there is a dummy-project `conanfile` which contains the following dependency diagraph

![Default Output](/example/default-conan-info-dot-template.png?raw=true)

With the _beautified conan info dot template_ provided in this repository, the ouput is like follows

![Beautified Output](/example/beautified-conan-info-dot-template.png?raw=true)

