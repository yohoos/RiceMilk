<template>
  <v-btn color="red" dark @click="logout">Logout</v-btn>
</template>

<script>
//  import axios from 'axios'

  export default {
    methods: {
      logout: function () {
        // axios call to backend to remove http only cookie
        this.$store.dispatch('removeAuth')
      }
    }
  }
</script>
