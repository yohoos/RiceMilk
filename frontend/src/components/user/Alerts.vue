<template>
  <div>
    <v-dialog v-model="refreshDialog" max-width="500px">
      <v-card>
        <v-card-title class="justify-center">
          <span class="headline text-xs-center">Login Expiring Soon</span>
        </v-card-title>
        <v-card-text>
          Click the refresh button below to refresh your login.
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green" @click="refresh()">Refresh</v-btn>
          <v-btn color="red" @click.stop="refreshDialog=false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="expiredDialog" max-width="500px">
      <v-card>
        <v-card-title class="justify-center">
          <span class="headline text-xs-center">Login Expired</span>
        </v-card-title>
        <v-card-text>
          Your login has expired. Please login again by typing in your credentials in the login prompt.
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" @click.stop="expiredDialog=false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data: () => ({
      refreshDialog: false,
      expiredDialog: false
    }),
    methods: {
      refresh: function () {
        axios.post('/user_auth/api_token_refresh')
          .then(response => {
            this.$store.dispatch('setAuth', response.data['expires'])
            this.refreshDialog = false
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    computed: {
      expiring: function () {
        return this.$store.getters.expiration !== 0 &&
          this.$store.getters.timeLeft <= 30000 && this.$store.getters.timeLeft > 0
      },
      expired: function () {
        return this.$store.getters.timeLeft <= 0 && this.$store.getters.expiration !== 0
      }
    },
    watch: {
      expiring: function (val) {
        if (val === true) {
          this.refreshDialog = true
        }
      },
      expired: function (val) {
        if (val === true) {
          this.refreshDialog = false
          this.expiredDialog = true
        }
      }
    }
  }
</script>
