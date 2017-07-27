'use strict'

angular.module('lineGraph').controller("LineCtrl", function ($scope) {
	
  
  $scope.colors = ['#00ADF9','#803690', '#00ADF9', '#DCDCDC', '#46BFBD', '#FDB45C', '#949FB1', '#4D5360'];
  $scope.labels = [0, 25, 50, 75, 100, 125, 150, 175, 200, 225];
  $scope.series = ['Graph 1', 'Graph 2','Graph 3', 'Graph 4','Graph 5'];
  $scope.data = [
    [65, 59, 80, 81, 56, 55, 40,12, 67,76],
	[],
     //[28, 48, 40, 19, 86, 27, 90,17,83,35],
  ];
  
 /* $scope.data2 = [
	[28, 48, 40, 19, 86, 27, 90,17,83,35],
      [65, 59, 80, 81, 56, 55, 40,12, 67,76],
  ];*/
  
  $scope.datasetOverride = [{ yAxisID: 'y-axis-1' }, { yAxisID: 'y-axis-2' }];
  $scope.options = {
    scales: {
      yAxes: [
        {
          id: 'y-axis-1',
          type: 'linear',
          display: true,
          position: 'left',
		  
        },
        {
          id: 'y-axis-2',
          type: 'linear',
          display: false,
          position: 'right',
        }
      ]
    }
  };
  
  
  $scope.randomize = function () {
      $scope.data = $scope.data.map(function (data) {
        return data.map(function (y) {
          y = y + Math.random() * 10 - 5;
          return parseInt(y < 0 ? 0 : y > 100 ? 100 : y);
        });
      });
    };
	
	$scope.clear = function () {
      $scope.data = [[0],[0]];
    };
	
	$scope.change = function (x, y) 
	{	
	for(var i = 0; i<y.length;i++) $scope.data[0][i] = y[i];	
	for(var i = 0; i<x.length;i++) $scope.labels[i] = x[i];	

    };
	
	$scope.change1 = function (x, y) 
	{	
	for(var i = 0; i<y.length;i++) $scope.data[1][i] = y[i];	
	for(var i = 0; i<x.length;i++) $scope.labels[i] = x[i];	
    };
});