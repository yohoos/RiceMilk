<template>
  <v-btn color="red" dark @click="logout">Logout</v-btn>
</template>

<script>
  import axios from 'axios'

  export default {
    methods: {
      logout: function () {
        axios.post('/user_auth/api_token_logout')
          .catch(error => {
            console.log('Error logging out: ' + error)
          })
        this.$store.dispatch('removeAuth')
      }
    }
  }
</script>
