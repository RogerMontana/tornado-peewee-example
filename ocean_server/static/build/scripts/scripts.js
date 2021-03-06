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
    'ngCart.fulfilment', 
    'ui.bootstrap',
    'GoogleMapsNative',
    'google.places'
  ])
  .config(function ($routeProvider,$httpProvider, $locationProvider, $rootScopeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: '/static/build/views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/about', {
        templateUrl: '/static/build/views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .when('/gifts', {
        templateUrl: '/static/build/views/gifts.html',
        controller: 'GiftsCtrl',
        controllerAs: 'gifts'
      })
      .when('/how', {
        templateUrl: '/static/build/views/how.html',
        controller: 'HowCtrl',
        controllerAs: 'how'
      })
      .when('/rocket04', {
        templateUrl: '/static/build/views/store.html',
        controller: 'storeCtrl',
        controllerAs: 'store'
      })
      // .when('/cart', {
      //   templateUrl: '/static/build/views/cart.html',
      //   controller: 'cartCtrl',
      //   controllerAs: 'cart'
      // })
      .when('/desc/:id', {
        templateUrl: '/static/build/views/fulldesc.html',
        controller: 'FulldescCtrl',
        controllerAs: 'f'
      })
      .when('/gMap', {
        templateUrl: '/static/build/views/gmap.html',
        controller: 'GmapCtrl',
        controllerAs: 'gMap'
      })
      .when('/contract', {
        templateUrl: '/static/build/views/contract.html',
        controller: 'ContractCtrl',
        controllerAs: 'contract'
      })
      .when('/contacts', {
        templateUrl: '/static/build/views/contacts.html',
        controller: 'ContactsCtrl',
        controllerAs: 'contacts'
      })
      .otherwise({
        redirectTo: '/'
      });

      // $locationProvider.html5Mode(true);
  }).run(['$location',function($scope){
    $scope.storeLoader = false;
    $('#menuStick').slicknav({
      brand:"<a href=\"#/\"><img src=\"https://rocket04.imgix.net/logo.svg?s=533089706d3998f2811d218fd2fe2fa5\" alt=\"\"></a>",
      label:"  ",
      closeOnClick: true
    });

    $scope.centerin = function centerin () {
      var b = (((document.body.clientWidth - 120) / 2)/document.body.clientWidth)*100;
      var c = b + "%";
      $('.slicknav_brand').css('left', c);
      $('.navbar-header').css('left', c);

      var f = (((document.body.clientWidth - 105) / 2)/document.body.clientWidth)*100;
      var a = f + "%";
      $('.spinner').css ('left', a);
    };
    $(window).resize(function(){
      $scope.centerin();
    });
    $scope.centerin();
  }]).animation('.rocket-view', function() {
    return {
      enter: function(element, done) {
        element.css('display', 'none');
        element.fadeIn(100, done);
        return function() {
          element.stop();
        };
      },
      leave: function(element, done) {
        element.fadeOut(100, done);
        return function() {
          element.stop();
        };
      }
    };
  });
'use strict';

//first module
angular.module('ocean04App')

    .config([function () {

    }])

    .provider('$ngCart', function () {
        this.$get = function () {
        };
    })

    .run(['$rootScope', 'ngCart','ngCartItem', 'store', function ($rootScope, ngCart, ngCartItem, store) {

        $rootScope.$on('ngCart:change', function(){
            ngCart.$save();
        });

        if (angular.isObject(store.get('cart'))) {
            ngCart.$restore(store.get('cart'));

        } else {
            ngCart.init();
        }

    }])

    .service('ngCart', ['$rootScope', 'ngCartItem', 'store', function ($rootScope, ngCartItem, store) {

        this.init = function(){
            this.$cart = {
                shipping : null,
                taxRate : null,
                tax : null,
                items : []
            };
        };

        this.addItem = function (id, name, price, quantity, data) {

            var inCart = this.getItemById(id);

            if (typeof inCart === 'object'){
                //Update quantity of an item if it's already in the cart
                inCart.setQuantity(quantity, false);
            } else {
                var newItem = new ngCartItem(id, name, price, quantity, data);
                this.$cart.items.push(newItem);
                $rootScope.$broadcast('ngCart:itemAdded', newItem);
            }

            $rootScope.$broadcast('ngCart:change', {});
        };

        this.getItemById = function (itemId) {
            var items = this.getCart().items;
            var build = false;

            angular.forEach(items, function (item) {
                if  (item.getId() === itemId) {
                    build = item;
                }
            });
            return build;
        };

        this.setShipping = function(shipping){
            this.$cart.shipping = shipping;
            return this.getShipping();
        };

        this.getShipping = function(){
            if (this.getCart().items.length == 0) return 0;
            return  this.getCart().shipping;
        };

        this.setTaxRate = function(taxRate){
            this.$cart.taxRate = +parseFloat(taxRate).toFixed(2);
            return this.getTaxRate();
        };

        this.getTaxRate = function(){
            return this.$cart.taxRate
        };

        this.getTax = function(){
            return +parseFloat(((this.getSubTotal()/100) * this.getCart().taxRate )).toFixed(2);
        };

        this.setCart = function (cart) {
            this.$cart = cart;
            return this.getCart();
        };

        this.getCart = function(){
            return this.$cart;
        };

        this.getItems = function(){
            return this.getCart().items;
        };

        this.getTotalItems = function () {
            var count = 0;
            var items = this.getItems();
            angular.forEach(items, function (item) {
                count += item.getQuantity();
            });
            return count;
        };

        this.getTotalUniqueItems = function () {
            return this.getCart().items.length;
        };

        this.getSubTotal = function(){
            var total = 0;
            angular.forEach(this.getCart().items, function (item) {
                total += item.getTotal();
            });
            return +parseFloat(total).toFixed(2);
        };

        this.totalCost = function () {
            return +parseFloat(this.getSubTotal() + this.getShipping() + this.getTax()).toFixed(2);
        };

        this.removeItem = function (index) {
            this.$cart.items.splice(index, 1);
            $rootScope.$broadcast('ngCart:itemRemoved', {});
            $rootScope.$broadcast('ngCart:change', {});

        };

        this.removeItemById = function (id) {
            var cart = this.getCart();
            angular.forEach(cart.items, function (item, index) {
                if  (item.getId() === id) {
                    cart.items.splice(index, 1);
                }
            });
            this.setCart(cart);
            $rootScope.$broadcast('ngCart:itemRemoved', {});
            $rootScope.$broadcast('ngCart:change', {});
        };

        this.empty = function () {
            
            $rootScope.$broadcast('ngCart:change', {});
            this.$cart.items = [];
            localStorage.removeItem('cart');
        };
        
        this.isEmpty = function () {
            
            return (this.$cart.items.length > 0 ? false : true);
            
        };

        this.toObject = function() {

            if (this.getItems().length === 0) return false;

            var items = [];
            angular.forEach(this.getItems(), function(item){
                items.push (item.toObject());
            });

            return {
                shipping: this.getShipping(),
                tax: this.getTax(),
                taxRate: this.getTaxRate(),
                subTotal: this.getSubTotal(),
                totalCost: this.totalCost(),
                items:items
            }
        };


        this.$restore = function(storedCart){
            var _self = this;
            _self.init();
            _self.$cart.shipping = storedCart.shipping;
            _self.$cart.tax = storedCart.tax;

            angular.forEach(storedCart.items, function (item) {
                _self.$cart.items.push(new ngCartItem(item._id,  item._name, item._price, item._quantity, item._data));
            });
            this.$save();
        };

        this.$save = function () {
            return store.set('cart', JSON.stringify(this.getCart()));
        }

    }])

    .factory('ngCartItem', ['$rootScope', '$log', function ($rootScope, $log) {

        var item = function (id, name, price, quantity, data) {
            this.setId(id);
            this.setName(name);
            this.setPrice(price);
            this.setQuantity(quantity);
            this.setData(data);
        };


        item.prototype.setId = function(id){
            if (id)  this._id = id;
            else {
                $log.error('An ID must be provided');
            }
        };

        item.prototype.getId = function(){
            return this._id;
        };


        item.prototype.setName = function(name){
            if (name)  this._name = name;
            else {
                $log.error('A name must be provided');
            }
        };
        item.prototype.getName = function(){
            return this._name;
        };

        item.prototype.setPrice = function(price){
            var priceFloat = parseFloat(price);
            if (priceFloat) {
                if (priceFloat <= 0) {
                    $log.error('A price must be over 0');
                } else {
                    this._price = (priceFloat);
                }
            } else {
                $log.error('A price must be provided');
            }
        };
        item.prototype.getPrice = function(){
            return this._price;
        };


        item.prototype.setQuantity = function(quantity, relative){


            var quantityInt = parseInt(quantity);
            if (quantityInt % 1 === 0){
                if (relative === true){
                    this._quantity  += quantityInt;
                } else {
                    this._quantity = quantityInt;
                }
                if (this._quantity < 1) this._quantity = 1;

            } else {
                this._quantity = 1;
                $log.info('Quantity must be an integer and was defaulted to 1');
            }
            $rootScope.itemQuantity = this._quantity;
            $rootScope.$broadcast('ngCart:change', {});

        };

        item.prototype.getQuantity = function(){
            return this._quantity;
        };

        item.prototype.setData = function(data){
            if (data) this._data = data;
        };

        item.prototype.getData = function(){
            if (this._data) return this._data;
            else $log.info('This item has no data');
        };


        item.prototype.getTotal = function(){
            return +parseFloat(this.getQuantity() * this.getPrice()).toFixed(2);
        };

        item.prototype.toObject = function() {
            return {
                id: this.getId(),
                name: this.getName(),
                price: this.getPrice(),
                quantity: this.getQuantity(),
                data: this.getData(),
                total: this.getTotal()
            }
        };

        return item;

    }])

    .service('store', ['$window', function ($window) {

        return {

            get: function (key) {
                if ($window.localStorage [key]) {
                    var cart = angular.fromJson($window.localStorage [key]);
                    return JSON.parse(cart);
                }
                return false;

            },


            set: function (key, val) {

                if (val === undefined) {
                    $window.localStorage .removeItem(key);
                } else {
                    $window.localStorage [key] = angular.toJson(val);
                }
                return $window.localStorage [key];
            }
        }
    }])

    .controller('CartController',['$scope', 'ngCart', function($scope, ngCart) {
        $scope.ngCart = ngCart;

    }])

    .value('version', '1.0.0');
;'use strict';

//second module
angular.module('ocean04App')

    .controller('CartController',['$rootScope','$scope', 'ngCart', function($rootScope,$scope, ngCart) {
        $scope.ngCart = ngCart;
    }])

    .directive('ngcartAddtocart', ['ngCart', function(ngCart){
        return {
            restrict : 'E',
            controller : 'CartController',
            scope: {
                id:'@',
                name:'@',
                quantity:'@',
                quantityMax:'@',
                price:'@',
                data:'='
            },
            transclude: true,
            templateUrl: function(element, attrs) {
                if ( typeof attrs.templateUrl == 'undefined' ) {
                    return 'static/build/views/directives/ngCart/addtocart.html';
                } else {
                    return attrs.templateUrl;
                }
            },
            link:function(scope, element, attrs){
                scope.attrs = attrs;
                scope.inCart = function(){
                    return  ngCart.getItemById(attrs.id);
                };

                if (scope.inCart()){
                    scope.q = ngCart.getItemById(attrs.id).getQuantity();
                } else {
                    scope.q = parseInt(scope.quantity);
                }

                scope.qtyOpt =  [];
                for (var i = 1; i <= scope.quantityMax; i++) {
                    scope.qtyOpt.push(i);
                }

            }

        };
    }])

    .directive('ngcartCart', [function(){
        return {
            restrict : 'E',
            controller : 'CartController',
            scope: {},
            templateUrl: function(element, attrs) {
                if ( typeof attrs.templateUrl == 'undefined' ) {
                    return 'static/build/views/directives/ngCart/cart.html';
                } else {
                    return attrs.templateUrl;
                }
            },
            link:function(scope, element, attrs){

            }
        };
    }])

    .directive('ngcartSummary', [function(){
        return {
            restrict : 'E',
            controller : 'CartController',
            scope: {},
            transclude: true,
            templateUrl: function(element, attrs) {
                if ( typeof attrs.templateUrl == 'undefined' ) {
                    return 'static/build/views/directives/ngCart/summary.html';
                } else {
                    return attrs.templateUrl;
                }
            }
        };
    }])

    .directive('ngcartCheckout', [function(){
        return {
            restrict : 'E',
            controller : ('CartController', ['$rootScope', '$scope', 'ngCart', 'fulfilmentProvider', function($rootScope, $scope, ngCart, fulfilmentProvider) {
                $scope.ngCart = ngCart;

                $scope.checkout = function () {
                    fulfilmentProvider.setService($scope.service);
                    fulfilmentProvider.setSettings($scope.settings);
                    fulfilmentProvider.checkout()
                        .success(function (data, status, headers, config) {
                            $rootScope.$broadcast('ngCart:checkout_succeeded', data);
                        })
                        .error(function (data, status, headers, config) {
                            $rootScope.$broadcast('ngCart:checkout_failed', {
                                statusCode: status,
                                error: data
                            });
                        });
                }
            }]),
            scope: {
                service:'@',
                settings:'='
            },
            transclude: true,
            templateUrl: function(element, attrs) {
                if ( typeof attrs.templateUrl == 'undefined' ) {
                    return 'static/build/views/directives/ngCart/checkout.html';
                } else {
                    return attrs.templateUrl;
                }
            }
        };
    }]);
;

//third module
angular.module('ngCart.fulfilment', [])
    .service('fulfilmentProvider', ['$injector', function($injector){

        this._obj = {
            service : undefined,
            settings : undefined
        };

        this.setService = function(service){
            this._obj.service = service;
        };

        this.setSettings = function(settings){
            this._obj.settings = settings;
        };

        this.checkout = function(){
            var provider = $injector.get('ngCart.fulfilment.' + this._obj.service);
              return provider.checkout(this._obj.settings);

        }

    }])


.service('ngCart.fulfilment.log', ['$q', '$log', 'ngCart', function($q, $log, ngCart){

        this.checkout = function(){

            var deferred = $q.defer();

            $log.info(ngCart.toObject());
            deferred.resolve({
                cart:ngCart.toObject()
            });

            return deferred.promise;

        }

 }])

.service('ngCart.fulfilment.http', ['$http', 'ngCart', function($http, ngCart){

        this.checkout = function(settings){
            return $http.post(settings.url,
                { data: ngCart.toObject(), options: settings.options});
        }
 }])


.service('ngCart.fulfilment.paypal', ['$http', 'ngCart', function($http, ngCart){


}]);

'use strict';

/**
 * @ngdoc service
 * @name ocean04App.loader
 * @description
 * # loader
 * Service in the ocean04App.
 */
angular.module('ocean04App')
  .service('loader', function ($http,$rootScope,$window,$location) {
    return{
      allowed:function (){
        $rootScope.storeLoader = false;
        $('.loader').css('display','none');
      }, 
      notAllowed: function () {
        $rootScope.storeLoader = true;
        $('.loader').css('display','block');
      },
      gaTitleScroll: function (title) {
        $rootScope.pagetitle = title;
        $(document).scrollTop(0);
        $window.ga('send', 'pageview', { page: $location.url() });
      }
    }
  });

'use strict';

angular.module('ocean04App')
  .service('api', function ($http,$q,$window) {
    $http.defaults.useXDomain = true;
     $http.defaults.headers.post["Content-Type"] = "text/plain";
    var url = 'https://rocket04.com/'

// MAIN API REQUEST METHODS
    var list =  function (suburl,field,param){
      return $q(function(resolve, reject) {
        $http({
          method:'GET',
          url: url+suburl,
          params:param
        }).success(function (data) {
          for(var i = 0; i<data.length; i++){
            var oldPrice = data[i].price.toString().split(".");
            data[i].price;
            data[i].newPrice = {
              grand:oldPrice[0],
              cents:oldPrice[1]
            }
          }
          localStorage.setItem('items', JSON.stringify(data));
          resolve(data);
        }).error(function (data, status, headers, config) {
          if(reject){
            reject(data);
          }
        });
      });
    };

    var post = function(suburl,param){
      return $q(function(resolve, reject) {
         $http.post(url+suburl,param)
        .success(function (data) {
          resolve(data);
        }).error(function (data, status, headers, config) {
          var a = JSON.stringify(arguments);
          alert(a);
          reject(data);
        });
      });
    };

//API functionality
    return {
      receipe: {
        store: function () {
          return list('get_recipes');
        },
        orders: function (order) {
          return post('order', order);
        },
        discount: function (code) {
          return post('promo', code);
        }
      }
    };
  });

'use strict';

/**
 * @ngdoc function
 * @name ocean04App.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the ocean04App
 */
angular.module('ocean04App').controller('MainCtrl', function (loader) {
	loader.gaTitleScroll("Главная Страница");
});

'use strict';
/**
 * @ngdoc function
 * @name ocean04App.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the ocean04App
 */
angular.module('ocean04App').controller('AboutCtrl', function (loader) {
	loader.gaTitleScroll("О Нас");
});

"use strict";

/**
 * @ngdoc function
 * @name ocean04App.controller:GiftsCtrl
 * @description
 * # GiftsCtrl
 * Controller of the ocean04App
 */
angular.module("ocean04App")
  .controller("GiftsCtrl", function ($scope, api, loader) {
    loader.gaTitleScroll("Подарки");
    $scope.gifts = [
      {
        img:"https://rocket04.imgix.net/gifts_1.jpg?s=fa9dea2977649ce50e30185840863067",
        price:50,
        text:"Быстро. Вкусно. Надёжно. Идеальный вариант, если других вариантов нет.",
        id:1,
        popular:""
      },{
        img:"https://rocket04.imgix.net/gifts_2.jpg?s=77307f3ac2cd865f502625a63ad84970",
        id:2,
        price:100,
        text:"Идеально, что бы закрыть углеводное окно",
        popular:""
      },{
        img:"https://rocket04.imgix.net/gifts_3.jpg?s=67d0cef4aafa8c934c57a971ee6f4e22",
        id:3,
        price:250,
        text:"Перфекто для мистер или миссис Эгоисто на уно вечер",
        popular:"Популярное"
      },{
        img:"https://rocket04.imgix.net/gifts_4.jpg?s=bf19b02e7d7a5a76de7773444db6656f",
        id:4,
        price:500,
        text:"Идеальные выходные без головной боли на двоих",
        popular:""
      }
    ];
  	var giftCards = $(".giftCard");
    $("#phone").mask("+38(999)999-99-99");
    $scope.formUser = {};
  	$scope.selectedGift;

  	$scope.selectGift = function(id, gift){
  		$scope.selectedGift = id;
      $scope.formUser.order_details = "Подарочный сертификат стоимостью: " + gift.price;
  	}

    $scope.buyGift = function () {
      var newPhone = [];
      for (var i = 0; i<$scope.formUser.phone.length;i++){
        if($scope.formUser.phone[i] !== ")"){
          if($scope.formUser.phone[i] !== "("){
            if($scope.formUser.phone[i] !== "-"){
              newPhone.push($scope.formUser.phone[i]);
            }
          }
        } 
      }
      $scope.formUser.phone = newPhone.join('');
      api.receipe.orders($scope.formUser).then(function(response){
        $scope.notification = true;
        $scope.successOrder = true;
      },function(err) {
        $scope.notification = true;
        $scope.errorOrder = true;
      });
    }
  });

'use strict';
/**
 * @ngdoc function
 * @name ocean04App.controller:HowCtrl
 * @description
 * # HowCtrl
 * Controller of the ocean04App
 */
angular.module('ocean04App').controller('HowCtrl', function (loader) {
	loader.gaTitleScroll("Принцип Работы");
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
  .controller('storeCtrl', function ($scope, $rootScope, api, loader, ngCart, ngCartItem, $interval, $timeout) {
    loader.gaTitleScroll("Ежедневное Меню");
    $rootScope.itemDescription = false;
    $(".slicknav_menu").show();
    $scope.receipeLst1 = [];
    $scope.colourIncludes = [];

    //getting data from server Artem
    this.getReceipesList = function() {
      loader.notAllowed();
      api.receipe.store().then(function(response) {
        $scope.receipeLst1 = response;
        loader.allowed();
      }, function(err) {
        $scope.receipeLst1 = [];
        loader.allowed();
      });
    };

    var countDownTimer = new Date().getHours();
    $scope.countDownFlag = false;

    if(countDownTimer == 17){
      $scope.countDownFlag = true;
      $scope.countDown = 59-new Date().getMinutes();
      $interval(function() {
        $scope.countDown = $scope.countDown - 1
        if ($scope.countDown == 0){
          $scope.stopCountDown();
          $scope.countDownFlag = false;
        }
        console.log($scope.countDown);
      }, 60000);
    }

    $scope.stopCountDown = function() {
      if (angular.isDefined(stop)) {
        $interval.cancel(stop);
        stop = undefined;
      }
    };

    $scope.includeColour = function(colour) {
      var i = $.inArray(colour, $scope.colourIncludes);
      if (i > -1) {
        $scope.colourIncludes.splice(i, 1);
      } else {
        $scope.colourIncludes.push(colour);
      }
    }
      
    $scope.colourFilter = function(fruit) {
      if ($scope.colourIncludes.length > 0) {
        if ($.inArray(fruit.tag, $scope.colourIncludes) < 0)
          return;
      }  
      return $scope.receipeLst1;
    }

    $scope.clearFilter = function () {
      $scope.colourIncludes = [];
      $('input[type="checkbox"]').prop( "checked", false ).parent().css('background', 'white');
    }

    //getting quantity in cart by its id 
    this.getInCartQuantity = function (id) {
      // // var inCartQunatity = ngCart.getItemById(id);
      // // var a = inCartQunatity._quantity;
      // // this.inCartQunatity = ngCart.getItemById(id)._quantity;
      // // return this.inCartQunatity;      
      return ngCart.getItemById(id)._quantity;
    };

    //removing or decrementing item quantity in cart
    this.removeFromCart = function (id) {
      // var inCart = ngCart.getItemById(id);
      // if(inCart._quantity === 1){
      //   ngCart.removeItemById(id);
      // }else if(inCart._quantity > 1){
      //   inCart.setQuantity(-1, true)
      // }else{
      //   return;
      // }
      ngCart.getItemById(id)._quantity === 1 ? 
        ngCart.removeItemById(id) : 
          ngCart.getItemById(id).setQuantity(-1, true);

      this.getInCartQuantity(id);
      // this.showQuantity(id);
    };

    //adding or incrementing item quantity in cart
    this.AddToCart = function (id, name, price, q, data) {
      if(ngCart.getItemById(id)._quantity >= 1) q = ngCart.getItemById(id)._quantity + 1;
      ngCart.addItem(id, name, price, q, data);
      this.getInCartQuantity(id);
      // this.showQuantity(id);
    };

    $(window).scroll(function(){
      if ($(window).scrollTop() >= 79) $('.storeNav').addClass('fixed');
      else $('.storeNav').removeClass('fixed');
    });

    this.getReceipesList();
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
  .controller('cartCtrl', function ($scope, $rootScope, $timeout, loader, ngCart, api) {
    loader.gaTitleScroll("Корзина");
    $("#phone").mask("+38(999)999-99-99");
    $(".slicknav_menu").show();
    $rootScope.itemDescription = false;
    $scope.formUser = {email:""};
    $scope.delivery;
    $scope.address = {};
    $scope.discount ={
      code: ''
    };
    $scope.timeGaps = [];
    var timeGaps = [
      {
        isAvailable: true,
        gap: "НА СЕЙЧАС",
        isActive: true
      },{
        isAvailable: true,
        gap: "18.00 - 19.00",
        isActive: false
      },{
        isAvailable: true,
        gap: "19.00 - 20.00",
        isActive: false
      },{
        isAvailable: true,
        gap: "20.00 - 21.00",
        isActive: false
      },{
        isAvailable: true,
        gap: "21.00 - 22.00",
        isActive: false
      }
    ];

    $scope.selectedGap = timeGaps[0].gap;

    var monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"];

    $scope.checkShipping = function (km) {
      ngCart.totalCost()>500 ? $scope.shipping = 0 : $scope.shipping = 50;
      if($scope.shipping == 50){
        km>5 ? $scope.shipping=Math.round(((km-5)*0.5+$scope.shipping)) : $scope.shipping = 50;
      }
    };

    $scope.getWeekDay = function (i) {
      if(new Date().getHours() >= 18) i=i+1;
      return {
        day:[
          "Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб",
          "Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб",
          "Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб",
          "Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"
        ][new Date().getDay()+i],
        date:new Date(+new Date()+(86400000*i)).getDate(),
        originalDate: new Date(+new Date()+(86400000*i)),
        isActive:false 
      };
    };

    $scope.setDeliveryDates = function(){
      $scope.dates = [$scope.getWeekDay(0)];
      $scope.dates[0].isActive = true;
      $scope.deliveryDate = $scope.dates[0].originalDate;
      for (var i=1;i<6;i++) $scope.dates.push($scope.getWeekDay(i));
    };

    $scope.setDeliveryDates();

    $scope.$watch("address", function (data) {
      if(data.geometry){
        var coor = {
          lat:data.geometry.location.lat(),
          lng:data.geometry.location.lng()
        };
        $scope.getDirection(coor);
      }
    });

    $scope.getDirection = function (address) {
      var directionsService = new google.maps.DirectionsService(),
          start = new google.maps.LatLng(48.466392, 35.025341),
          end = new google.maps.LatLng(address.lat, address.lng),
          bounds = new google.maps.LatLngBounds();
      bounds.extend(start);
      bounds.extend(end);
      var request = {
        origin: start,
        destination: end,
        travelMode: google.maps.TravelMode.DRIVING
      };
      directionsService.route(request, function (response, status) {
        if (status == google.maps.DirectionsStatus.OK)
          $scope.checkShipping(response.routes[0].legs[0].distance.value / 1000);
      });
    };

    $scope.setActiveDelivery = function (choosen){
      $scope.dates.forEach(function (key) {key.isActive = false;});
      $scope.dates[$scope.dates.indexOf(choosen)].isActive = true;
      $scope.deliveryDate = choosen.originalDate;
    };

    $scope.cartItems = ngCart.getCart();

    $scope.getCart = function(){
      $scope.cartTotal = ngCart.totalCost();
    };

    $scope.autocompleteOptions = {
      componentRestrictions: { country: 'ua' }
    };

    $scope.removeItem = function(id){
      ngCart.removeItemById(id);
    };

    $scope.countTotal = function () {
      $scope.checkShipping();
      $scope.totalWithShipping = ngCart.totalCost() + $scope.shipping;
      $scope.percent = '';
    };

    $scope.enterPress = function(e){
      if(e.keyCode == 13){
        $scope.discountCheck();
      }
    };

    $scope.destroyUI = function () {
      localStorage.removeItem('cart');
      $scope.formUser = {email:""};
      $scope.cartItems = {};
      $scope.cartTotal = 0;
      $scope.address = {};
    };

    $scope.setGap = function (gap){
      $scope.selectedGap = gap.gap;
    };

    $scope.checkGaps = function () {
      var checkGap = new Date().getHours();
      if(checkGap >= 18 || checkGap<=10){
        $scope.selectedGap = timeGaps[1].gap;
        timeGaps[0].isAvailable = false;
        timeGaps[0].isActive = false;
        timeGaps[1].isActive = true;
        timeGaps.forEach(function(key){
          $scope.timeGaps.push(key);
        });
      }else{
        $scope.timeGaps = timeGaps;
      }
    };

    $scope.getCart();
    $scope.checkShipping();
    $scope.countTotal();

    $scope.checkout = function () {
      $('#myModal').modal('show');
      if(!$scope.address.formatted_address)
        $scope.address.formatted_address = $('#adress').val();
      
      $scope.formUser.address = $scope.address.formatted_address;
      $scope.formUser.total = (ngCart.totalCost() + $scope.shipping);

      var order_details = [];
      ngCart.getCart().items.forEach(function (key) {
        order_details.push(key._name + " - " + key._quantity);
      });
      $scope.formUser.order_details = order_details.join(", ");

      var date = new Date($scope.deliveryDate).getDate()+' '+monthNames[new Date($scope.deliveryDate).getMonth()];
      var time = $scope.selectedGap;

      if(time == "НА СЕЙЧАС"){
        time = (new Date().getHours() + 3) + ":" + (new Date().getMinutes());
      }

      $scope.formUser.timegap = date + '|' + time;

      $scope.formUser.phone = "+"+$scope.formUser.phone.replace(/\W/g,"");
      console.log($scope.formUser);
    };

    $scope.discountCheck = function () {
      $scope.discountLoader = true;
      api.receipe.discount($scope.discount).then(function(data){
        $scope.totalWithShipping = $scope.totalWithShipping - ($scope.totalWithShipping/100*data.discount);
        $scope.percent = data.discount;
        if(data.discount == 0) {
          $scope.discountError = true;
        }
        $scope.discountLoader = false;
      }, function (err) {
        console.log(err);
        $scope.discountLoader = false;
      })
    }

    $scope.makeOrder = function () {
      $('#myModal').modal('hide');
      api.receipe.orders($scope.formUser).then(function(response){
        $scope.notification = true;
        $scope.successOrder = true;
        $scope.destroyUI ();
      },function(err) {
        $scope.notification = true;
        $scope.errorOrder = true;
      });
    }
    $scope.checkGaps();
  });

'use strict';

/**
 * @ngdoc function
 * @name ocean04App.controller:FulldescCtrl
 * @description
 * # FulldescCtrl
 * Controller of the ocean04App
 */
angular.module('ocean04App')
  .controller('FulldescCtrl', function ($scope, $rootScope, $routeParams, api, loader, ngCart) {
    $rootScope.itemDescription = true;
    $('.slicknav_menu').each(function () {
        this.style.setProperty( 'display', 'none', 'important' );
    });
    $scope.receipe;

    var that = this;

     this.checkLocal = function () {
      if(localStorage.getItem('items')){
        this.getRecepieById($routeParams.id);
      } else {
        this.getReceipesList();
      }
    }

    this.getReceipesList = function() {
      api.receipe.store().then(function(response) {
        $scope.receipeLst1 = response;
        that.getRecepieById($routeParams.id);
      }, function(err) {
        $scope.receipeLst1 = [];
        loader.allowed();
      });
    };

    this.getRecepieById = function (id) {
      var items = JSON.parse(localStorage.getItem('items')).filter(function (obj) {
        if(obj.id == id){
          return true;
        }
      });
      var data = items[0];
      var oldPrice = data.price.toString().split(".");
      var oldNutrients = data.nutrients.split("|");
      var subtitle = data.subtitle.split("|");
      data.ingredients = data.ingredients.split("|");
      data.portions = subtitle[0];
      data.time = subtitle[1];
      data.newPrice = {
        grand:oldPrice[0],
        cents:oldPrice[1]
      }
      data.slides=[];
      data.slides.push(data.photo);
      data.slides.push(data.ingredients_photo);
      data.newNutrients= {
        callories: oldNutrients[0],
        proteins: oldNutrients[1],
        fats: oldNutrients[2],
        carbohydrates: oldNutrients[3]
      };
      $scope.receipe = data;
      loader.gaTitleScroll($scope.receipe.title);
    }

    $scope.diet = [
      {
        img:'',
        name:'',
      },
      {
        img:'http://rocket04.imgix.net/diet_1.svg?s=4c4e6a0cab130c322c6aca083b5a3076',
        name:'Вегетарианское',
      },
      {
        img:'http://rocket04.imgix.net/diet_2.svg?s=086e988e8553d4028ed8e29377359fe6',
        name:'Веганское',
      },
      {
        img:'http://rocket04.imgix.net/diet_3.svg?s=85af099e62e0349cc057f83300d7482a',
        name:'Без Глютена',
      },
      {
        img:'http://rocket04.imgix.net/diet_4.svg?s=27c75e9d2a090988e06b640a6c457b72',
        name:'Без Лактозы',
      },
      {
        img:'http://rocket04.imgix.net/diet_5.svg?s=501744a476ede9d815c68ea228821fbc',
        name:'Без Орехов',
      },
      {
        img:'http://rocket04.imgix.net/diet_6.svg?s=58e666fdb84a3510d6005701d2a6b4a9',
        name:'Без Яиц',
      },
      {
        img:'http://rocket04.imgix.net/diet_7.svg?s=d111f8f6c71db9d42505f9c2199b3920',
        name:'Палеодиета',
      }
    ]

    //getting quantity in cart by its id 
    this.getInCartQuantity = function (id) {
      return ngCart.getItemById(id)._quantity;
    };

    //removing or decrementing item quantity in cart
    this.removeFromCart = function (id) {
      // var inCart = ngCart.getItemById(id);
      // if(inCart._quantity === 1){
      //   ngCart.removeItemById(id);
      // }else if(inCart._quantity > 1){
      //   inCart.setQuantity(-1, true)
      // }else{
      //   return;
      // }
      ngCart.getItemById(id)._quantity === 1 ? 
        ngCart.removeItemById(id) : 
          ngCart.getItemById(id).setQuantity(-1, true);
      this.getInCartQuantity(id);
    };

    //adding or incrementing item quantity in cart
    this.AddToCart = function (id, name, price, q, data) {
      if(ngCart.getItemById(id)._quantity >= 1) q = ngCart.getItemById(id)._quantity + 1;
      ngCart.addItem(id, name, price, q, data);
      this.getInCartQuantity(id);
    };

    this.checkLocal();
  });

'use strict';
/**
 * @ngdoc function
 * @name ocean04App.controller:GmapCtrl
 * @description
 * # GmapCtrl
 * Controller of the ocean04App
 */
angular.module('ocean04App').controller('GmapCtrl', function (loader) {
	loader.gaTitleScroll("Зона Доставки");
});

'use strict';

/**
 * @ngdoc function
 * @name ocean04App.controller:ContractCtrl
 * @description
 * # ContractCtrl
 * Controller of the ocean04App
 */
angular.module('ocean04App').controller('ContractCtrl', function (loader) {
  loader.gaTitleScroll("Приватность и Условия");
});

'use strict';

/**
 * @ngdoc function
 * @name ocean04App.controller:ContactsCtrl
 * @description
 * # ContactsCtrl
 * Controller of the ocean04App
 */
angular.module('ocean04App').controller('ContactsCtrl', function (loader) {
  loader.gaTitleScroll("Контакты");
});
