# DF-Visualizer

:dart: DF-Visualizer is a tool to visualize the expressiveness and analyzability of dataflow models. It is based on the work presented in [1] and aims to provide a user-friendly interface for exploring the hierarchy of dataflow models.

:computer: DF-Visualizer is written in Python using Qt framework. It is a straightforward implementation of the expressiveness and analyzability hierarchy presented in section VII of [1].

:bulb: As described in [1], the hierarchy is easily extensible, either to add new dataflow models or to add new features to evaluate dataflow models. Don't hesitate to do a pull request!

:rocket: Ready to explore my project? Checkout the [documentation](https://groumage.github.io/DFMoCCs-survey/Doxygen/index.html)!

## Project usage

The GUI can be run using docker:
```bash
docker build -t dfmoccsgui . && docker run -it --rm -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY dfmoccsgui
```
where `<path_to_hierarchy_file>` is the path to the JSON file containing the hierarchy. If no path is provided, the program will use the default hierarchy file `resources/hierarchy-example.json`.

If you manage to have all python dependencies installed, you can run the GUI without docker:
```bash
python3 source/classificationGUI.py
```
## Learning more

Check out the [documentation](https://groumage.github.io/DFMoCCs-survey/Doxygen/index.html) for more details on how to use the GUI and how to extend it.

## References

[1] G. Roumage, S. Azaiez, C. Faure and S. Louise, "An Extended Survey and a Comparison Framework for Dataflow Models of Computation and Communication", arXiv, 2025, https://arxiv.org/abs/2501.07273.