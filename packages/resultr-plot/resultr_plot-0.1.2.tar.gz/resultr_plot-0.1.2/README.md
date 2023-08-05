#  resultr-plot
> plotting part of [resultr](https://github.com/haykkh/resultr)

**note** it's very possible that I made mistakes so take what this gives with a bucketload of salt.

resultr-plot lets you:
  * plot a histogram of the results for a module in the bins: (0,40), (40,50), (50, 60), (60, 70), (80, 90), (90, 100)

## Usage example

Requires:
  * [Python 3](https://www.python.org/downloads/)
  * [pandas](https://pandas.pydata.org/) and [matplotlib](https://matplotlib.org/) for plotting
  * [python-inquirer](https://github.com/magmax/python-inquirer) for the user input


### Running resultr-plot

You can run interact with resultr using [inquirer](https://github.com/magmax/python-inquirer) prompts:

![ask demo](demoAsk.gif)

Or equivalently by passing arguments when you run resultr-plot:

![args demo](demoArgs.gif)

```sh
$ python resultr-plot.py -h 
  usage: resultr-plot.py [-h] [--plot]
                     [--exportplots EXPORTPLOTS] [--showplots] 
  
  Makes UCL PHAS results better
  
  optional arguments:
    -h, --help              show this help message and exit

    --plot, -p              plot the module results

    --exportplots, -ep EXPORTPLOTS
                            export all plots to /path/you/want/

    --showplots, -sp        show all plots

```


## Release History

 
* 0.1.2
    * added _howPlotArgs_ back, added arguments to pass _exportplots_ and _showplots_ 
* 0.1.1
    * removed as_posix from  _plotter_
* 0.1.0
    * The first proper release


## Meta

Hayk Khachatryan – hi@hayk.io

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/haykkh](https://github.com/haykkh/)

## Contributing

1. Fork it (<https://github.com/haykkh/resultr-plot/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
