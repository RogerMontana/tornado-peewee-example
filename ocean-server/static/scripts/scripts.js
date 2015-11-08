'use strict';

/**
 * @ngdoc overview
 * @name ocean04App
 * @description
 * # ocean04App
 *
 * Main module of the application.
 */
angular
  .module('ocean04App', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'rocketStore'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .when('/gifts', {
        templateUrl: 'views/gifts.html',
        controller: 'GiftsCtrl',
        controllerAs: 'gifts'
      })
      .when('/how', {
        templateUrl: 'views/how.html',
        controller: 'HowCtrl',
        controllerAs: 'how'
      })
      .when('/team', {
        templateUrl: 'views/team.html',
        controller: 'TeamCtrl',
        controllerAs: 'team'
      })
      .when('/rocket04', {
        templateUrl: 'views/modules/store/rocket04.html',
        controller: 'storeCtrl',
        controllerAs: 'store'
      })
    .when('/account', {
        templateUrl: 'views/modules/store/account.html',
        controller: 'accountCtrl',
        controllerAs: 'account'
      })
    .when('/cart', {
        templateUrl: 'views/modules/store/cart.html',
        controller: 'cartCtrl',
        controllerAs: 'cart'
      })
      .otherwise({
        redirectTo: '/'
      });
  });

'use strict';

/**
 * @ngdoc overview
 * @name ocean04App
 * @description
 * # ocean04App
 *
 * Main module of the application.
 */
angular
  .module('rocketStore', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ]);
'use strict';

/**
 * @ngdoc function
 * @name ocean04App.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the ocean04App
 */
angular.module('ocean04App')
  .controller('MainCtrl', function ($rootScope) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $rootScope.rocketStart = false;
  });

'use strict';

/**
 * @ngdoc function
 * @name ocean04App.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the ocean04App
 */
angular.module('ocean04App')
  .controller('AboutCtrl', function ($rootScope) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $rootScope.rocketStart = false;
  });

'use strict';

/**
 * @ngdoc function
 * @name ocean04App.controller:GiftsCtrl
 * @description
 * # GiftsCtrl
 * Controller of the ocean04App
 */
angular.module('ocean04App')
  .controller('GiftsCtrl', function ($rootScope) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $rootScope.rocketStart = false;
  });

'use strict';

/**
 * @ngdoc function
 * @name ocean04App.controller:HowCtrl
 * @description
 * # HowCtrl
 * Controller of the ocean04App
 */
angular.module('ocean04App')
  .controller('HowCtrl', function ($rootScope) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $rootScope.rocketStart = false;
  });

'use strict';

/**
 * @ngdoc function
 * @name ocean04App.controller:TeamCtrl
 * @description
 * # TeamCtrl
 * Controller of the ocean04App
 */
angular.module('ocean04App')
  .controller('TeamCtrl', function ($rootScope) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $rootScope.rocketStart = false;
  });

'use strict';

/**
 * @ngdoc function
 * @name ocean04App.controller:TeamCtrl
 * @description
 * # TeamCtrl
 * Controller of the ocean04App
 */
angular.module('rocketStore')
  .controller('storeCtrl', function ($scope, $rootScope) {
    $rootScope.rocketStart = true;
  });

'use strict';

/**
 * @ngdoc function
 * @name ocean04App.controller:TeamCtrl
 * @description
 * # TeamCtrl
 * Controller of the ocean04App
 */
angular.module('rocketStore')
  .controller('cartCtrl', function ($scope, $rootScope) {
    $rootScope.rocketStart = true;
  });

'use strict';

/**
 * @ngdoc function
 * @name ocean04App.controller:TeamCtrl
 * @description
 * # TeamCtrl
 * Controller of the ocean04App
 */
angular.module('rocketStore')
  .controller('accountCtrl', function ($scope, $rootScope) {
    $rootScope.rocketStart = true;
  });
