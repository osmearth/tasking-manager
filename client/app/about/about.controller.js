(function () {

    'use strict';

    /**
     * About controller which manages the about page
     */
    angular
        .module('taskingManager')
        .controller('aboutController', [aboutController]);

    function aboutController() {
        var vm = this;

        vm.sponsors = [
            {
                name: 'Mapbox',
                logo: '',
                url: 'https://mapbox.com'
            },
            {
                name: 'MapHubs',
                logo: '',
                url: 'https://maphubs.com'
            }
        ]
    }
})();
