import csv
# charts [[Test name], <Number of asserts>, <number of failed asserts>]

#read data from file


data_list = []
with open('TestAnalysisData.csv') as csv_file:
  file_reader = csv.reader(csv_file)
  for row in file_reader:
    data_list.append(row)

# new list is initialiyed with headers

chart_data = [data_list[0]]
for row in data_list[1:]:
  num_of_asserts = int(row[1])
  num_of_failed_asserts = int(row[2])
  chart_data.append([row[0],num_of_asserts, num_of_failed_asserts])

# create HTML for chart
from string import Template
html_string = Template("""<html>
<head>
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script>
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  function drawChart () {
    var data = google.visualization.arrayToDataTable([
       $labels,
       $data
      ],
      false); // 'false' means that the first row contains labels, not data.
  
    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  }
</script>
</head>
<body>
  <div id="chart_div" style="width:800; height:600"></div>
</body>
</html>""")

chart_data_str = ''
for row in chart_data[1:]:
  chart_data_str += '%s,\n'%row

completed_html = html_string.substitute(labels = chart_data[0], data = chart_data_str)

with open('challenge2Chart.html', 'w') as f:
  f.write(completed_html)