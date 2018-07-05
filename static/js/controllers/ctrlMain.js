app.controller("ctrlMain", function ($scope, dataService) {

    $scope.data = null;
    dataService.loadData().success(function (data) {
        $scope.data = data;
        console.log('Data loaded', data);
    })

    $scope.pageTitle = "Sakila Admin";     
});

/*
    console.log('ctrlMain loaded');

    var loadData = function() {
        dataService.loadData().then(success, error);
    }

    var success = function(data) {
        $scope.data = data;
        console.log('ctrlMain $scope.data:' , $scope.data);
    }

    var error = function() {
        console.log('hmmmm data load error');
    }

    loadData();
    
});
*/
