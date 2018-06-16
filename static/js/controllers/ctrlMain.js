app.controller("ctrlMain", function ($scope) {

    var nowVal = Date.now();

    $scope.screenMsg = "Hello World " + nowVal

    console.log('ctrlMain loaded');


});
