'use strict';

var app = angular.module('try', ['lineGraph',]);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[/');
    $interpolateProvider.endSymbol('/]');
  });