app.factory('dataService', function ($http) {
    return {
        loadData: function () {
            return $http.get('data/data.json'); 
        }
    };
});

/*
 
app.factory('dataService', function ($http, $q) {
	var self = this;

	self.data = undefined;

	return {
        loadData: function() {

          return $q(function(resolve, reject) {

            var error = function(message) {
              return function() {
                reject(message);
              }
            };
            var success = function(result) {
              self.data = result.data;
              resolve(result.data);
            };

            var errorFn = error('error while loading data');
              var url = 'data/data.json';
            $http.get(url,
              {
                 headers: {
                     'Cache-Control': 'no-cache'
                 }
              }).then(success, errorFn);
          });
        },
        getData: function() {
          return self.data;
        }
      }
});
*/