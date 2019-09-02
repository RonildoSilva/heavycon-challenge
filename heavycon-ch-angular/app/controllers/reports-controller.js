'use strict';

// Declare app level module which depends on views, and core components
angular.module('myApp', [
  'ngRoute',
  'myApp.version'
]).
controller('ReportController', function($scope, $http){
  
  $scope.users = [];
  $scope.reports = [];

  $http({
    method: 'GET',
    url: 'http://localhost:8000/users/'
  })
  .then(function (response){
    $scope.users = response.data;
    console.log(response.data);
  },function (error){
    console.log(error);
  });

  $scope.hasChanged = function() {
    var id = $scope.selectedUser;
    console.log(id);
    $scope.reports = $scope.loadReport(id);
  }

  $scope.loadReport = function(id){
    $http({
      method: 'GET',
      url: 'http://localhost:8000/report/'+id
    })
    .then(function (response){
      $scope.reports = response.data;
      console.log(response.data);
      return $scope.reports;
    },function (error){
      console.log(error);
      return [];
    });
  }
}).

/**
controller('ReportController', function($scope, $http){
  
    $scope.reports = [];
  
    $http({
      method: 'GET',
      url: 'http://localhost:8000/reports/'
    })
    .then(function (response){
      $scope.reports = response.data;
      console.log(response.data);
    },function (error){
      console.log(error);
    });
  
  }).
 */

config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
$locationProvider.hashPrefix('!');
}]);
