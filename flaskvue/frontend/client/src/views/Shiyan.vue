<template>
  <div class="container">
    <!-- <button type="button" class="btn btn-primary">{{ msg }}</button> -->
  </div>
</template>



<script>

// Encapsulated network request
import {request} from '@/network/request';
import {request_withdata} from '@/network/request';

// Validation form
// import { Field, Form } from 'vee-validate';

export default {
  name: "Shiyan",
  // components: {
  //   Field,
  //   Form,
  // },
  data() {
    return {
      name: "",
      messages: [],
      
    };
  },

  mounted() {
    // this.$socket.connect();
    
  },

  methods: {
    // isRequired(value) {
    //   return value ? true : 'This field is required';
    // },
    
  },

};
</script>
