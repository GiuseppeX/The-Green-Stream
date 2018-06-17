app.controller("ctrlAdminMain", function ($scope, dataService) {

    $scope.screenTitleFunc = function () {
        return "Admin";
    }   

    var loadData = function () {
        dataService.loadData().then(success, error);
    }

    var success = function (data) {
        $scope.data = data;
        console.log('ctrlAdminMain $scope.data:', $scope.data);
    }

    var error = function () {
        console.log('hmmmm data load error');
    }

    loadData();

    console.log('ctrlAdminMain loaded');
});
