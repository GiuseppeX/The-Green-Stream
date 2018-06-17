var app = angular.module("myAdminApp", ["ngMaterial"]);

app.config(function ($mdThemingProvider) {
    $mdThemingProvider.theme('default')
        .primaryPalette('blue-grey')
        .accentPalette('yellow')
        .backgroundPalette('blue-grey');
});
