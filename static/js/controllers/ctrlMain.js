app.controller("ctrlMain", function ($scope) {

    $scope.screenMsg = "Dave"

    $scope.screenMsgFunc = function () {
        return "Hello World, and nodejs!";
    }   

    console.log('ctrlMain loaded');

});
