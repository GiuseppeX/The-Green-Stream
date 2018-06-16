app.controller("ctrlMain", function ($scope, dataService) {

    console.log('ctrlMain loaded');

    var loadData = function() {
        dataService.loadData().then(success, error);
    }

    var success = function(data) {
        $scope.data = data;
        console.log('ctrlMain $scope.data:' , $scope.data);
        drawChart();
    }

    var error = function() {
        console.log('hmmmm data load error');
    }

    $scope.getWarningClass = function(tu_grade){
      var className = "";
      if(tu_grade == 'E'){
        className = 'warn';
      }

      return className;
    }

    loadData();
});
