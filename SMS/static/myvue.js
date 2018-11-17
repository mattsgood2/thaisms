var app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data: {
    message: 'VueJs '
},
    mounted: function() {
      this.getmessage();
    },
    methods: {
        getmessage: function(){
            this.loading = true;
        }
    }
})


// app.message = 'PIM';
// new Vue({
//   delimiters: ['[[', ']]'],
//   el: '#app',
//   data: {
//     message: 'Hello Vue.js!'
//   },
//   updated() {
//     console.log('test')
//   },
//   mounted() {
//   	this.message = 'Hello I worked ';
//   }
// })
