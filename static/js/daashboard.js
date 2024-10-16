google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        // var data = google.visualization.arrayToDataTable([
        //   ['X', 'Y'],
        //   [1, 2],
        //   [2, 4],
        //   [0, 4],
        //   [3, 6],
        //   [4, 4]
        // ]);
        var data = new google.visualization.DataTable();

        data.addColumn('number', 'Marks');
        data.addColumn('number', 'Math marks');
        data.addRows([
            [15, 1], [20, 1], [21, 1], [23, 1], [24, 1], [25, 1], [27, 1], [28, 2], [30, 2], [31, 2], [32, 1], [33, 2], [34, 4], [35, 4], [36, 3], [37, 4], [38, 4], [39, 6], [40, 2], [41, 7], [42, 5], [43, 7], [44, 13], [45, 11], [46, 8], [47, 10], [48, 7], [49, 10], [50, 10], [51, 14], [52, 12], [53, 8], [54, 15], [55, 18], [56, 19], [57, 18], [58, 21], [59, 29], [60, 19], [61, 26], [62, 32], [63, 21], [64, 25], [65, 26], [66, 21], [67, 29], [68, 28], [69, 24], [70, 23], [71, 21], [72, 23], [73, 22], [74, 30], [75, 25], [76, 22], [77, 18], [78, 11], [79, 19], [80, 23], [81, 23], [82, 27], [83, 25], [84, 20], [85, 13], [86, 11], [87, 10], [88, 15], [89, 11], [90, 11], [91, 9], [92, 11], [93, 4], [94, 6], [95, 3], [96, 6], [97, 4], [98, 5], [99, 4], [100, 9]
        ]);
        var options = {
            hAxis: {
                title: 'Marks'
              },
              vAxis: {
                title: 'Frequency'
              },
            title: 'Maths marks distribution',
            curveType: 'function',
          };

          var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
  
          chart.draw(data, options);
    }