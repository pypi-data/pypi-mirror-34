#  resultr
> Makes UCL PHAS results better

**note** it's very possible that I made mistakes so take what this gives with a bucketload of salt.

UCL Physics and Astronomy publishes the results for every year as a pdf with this format: 

**Candidate Number**|**Devcom**|**Module1**|**Mark**|**Module2**|**Mark**|**Module3**|**Mark**|**Module4**|**Mark**|**Module5**|**Mark**|**Module6**|**Mark**|**Module7**|**Mark**|**Module8**|**Mark**|**Provisional outcome**| 
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
ABCD0|100|PHAS0000|99|PHAS0001|98|PHAS0002|97|PHAS0003|96|PHAS0004|95|PHAS0005|94|PHAS0006|93|PHAS0007|92|P| 
ABCD1|24|PHAS0003|93|PHAS0001|55|PHAS0004|43|PHAS0007|40|PHAS0002|34|PHAS0006|25|PHAS0005|15|PHAS0000|3|>>| 

resultr lets you:
  * get your weighted average for a year
  * get your rank in your year
  * plot a histogram of the results for a module in the bins: (0,40), (40,50), (50, 60), (60, 70), (80, 90), (90, 100)
  * re-format the results by module (as below) and output to csv

output format:

**Devcom**|**PHAS0000**|**PHAS0001**|**PHAS0002**|**PHAS0003**|**PHAS0004**|**PHAS0005**|**PHAS0006**|**PHAS0007**|**Averages**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
100|99|98|97|96|95|94|93|92|95.5
24|3|55|34|93|43|15|25|40|39 

## Installation

```sh
$ pip install resultr
```

## Usage example

Requires:
  * [Python 3](https://www.python.org/downloads/)
  * [pandas](https://pandas.pydata.org/) and [matplotlib](https://matplotlib.org/) for plotting
  * [python-inquirer](https://github.com/magmax/python-inquirer) for the user input


### Making the PDF usable

You're going to need to convert the .pdf given by UCL into a csv, delimited with ','. To do this I used [smallpdf](https://smallpdf.com/pdf-to-excel)'s PDF to Excel converter (this makes an xlsx with a sheet for every page of the page of the pdf). Then I used [Google Docs](https://docs.google.com) to export each sheet as a csv, and combined them in a texteditor (note though that you should remove the heading lines (cand, devcom, module1, etc) from all pages apart from the first)


### Running resultr

You can run interact with resultr using [inquirer](https://github.com/magmax/python-inquirer) prompts:

![ask demo](demoAsk.gif)

Or equivalently by passing arguments when you run resultr:

![args demo](demoArgs.gif)

```sh
$ resultr -h 
  usage: resultr [-h] [--input INPUT] [--format FORMAT] [--plot]
                     [--exportplots EXPORTPLOTS] [--showplots] [--my]
                     [--year YEAR] [--rank] [--candidate CANDIDATE]
  
  Makes UCL PHAS results better
  
  optional arguments:
    -h, --help              show this help message and exit

    --input, -i INPUT
                            csv file to import

    --format, -f FORMAT
                            reformats results by module and exports it to file
                            specified

    --plot, -p              plot the module results

    --exportplots, -ep EXPORTPLOTS
                            export all plots to /path/you/want/

    --showplots, -sp        show all plots

    --my, -m                returns your weighted average for the year

    --year, -y YEAR         specify your year

    --rank, -r              returns your rank in the year

    --candidate, -c CANDIDATE
                            specify your candidate number
```


## Release History

* 0.1.10
    * Changed 'Cand' to 'CAND' in length
* 0.1.9
    * pass _args.exportplots_ and _args.showplots_ to _resultr\_plot.howPlotArgs_ 
* 0.1.8
    * changed entry_point to use __main__.py
* 0.1.7
    * added entry_point to setup.py (resultr) 
* 0.1.6
    * split into _resultr\_format_ and _resultr\_plot_
* 0.1.5
    * changed _matplotlib_ to run with _Agg_ 
* 0.1.4
    * added _matplotlib_ requirement in setup.py 
* 0.1.3
    * added _inquirer_ requirement in setup.py
* 0.1.2
    * added pip
* 0.1.1
    * Moved prompt and cli code from ``'__main__'`` to ``main()`` 
    * Changed name to _resultr_ cause cool
* 0.1.0
    * The first proper release


## Meta

Hayk Khachatryan – hi@hayk.io

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/haykkh](https://github.com/haykkh/)

## Contributing

1. Fork it (<https://github.com/haykkh/resultr/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
