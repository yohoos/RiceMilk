<template lang="html">
  <v-dialog v-model="dialog" persistent max-width="500px" v-if="hasJWT">
    <v-btn color="green" dark slot="activator">Login</v-btn>
    <v-card>
      <v-form v-model="valid" ref="form" lazy-validation>
        <v-card-title>
          <span class="headline">Please Enter Credentials</span>
        </v-card-title>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex xs12>
                <v-text-field
                 label="Username"
                 v-model="username"
                 :rules="usernameRules"
                 required
                ></v-text-field>
              </v-flex>
              <v-flex xs12>
                <v-text-field
                  label="Password"
                  type="password"
                  v-model="password"
                  :rules="passwordRules"
                  required
                ></v-text-field>
              </v-flex>
            </v-layout>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" @click.native="dialog = false; clear()">Close</v-btn>
          <v-btn color="green" @click.native="dialog = false; login()">Login</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from 'axios'

export default {
  data: function () {
    return {
      dialog: false,
      valid: false,
      username: null,
      usernameRules: [
        (v) => !!v || 'Username is required'
      ],
      password: null,
      passwordRules: [
        (v) => !!v || 'Password is required'
      ]
    }
  },
  methods: {
    login: function () {
      if (this.$refs.form.validate()) {
        // var formData = new FormData()
        // formData.append('username', this.username)
        // formData.append('password', this.password)

        axios.post('/user_auth/api_token_create', {
          username: this.username,
          password: this.password
        })
        .then(response => {
          this.dialog = false
          this.clear()
        })
        .catch(e => {
          console.log(e)
        })
      }
    },
    clear: function () {
      this.$refs.form.reset()
    }
  },
  computed: {
    hasJWT: function () {
      var name = 'JWT_Cookie'
      var cookie = document.cookie
      var prefix = name + '='
      var begin = cookie.indexOf('; ' + prefix)
      if (begin === -1) {
        begin = cookie.indexOf(prefix)
        if (begin !== 0) {
          return true
        }
      } else {
        begin += 2
        var end = document.cookie.indexOf(';', begin)
        if (end === -1) {
          end = cookie.length
        }
      }
      return false
      // return unescape(cookie.substring(begin + prefix.length, end));
    }
  }
}
</script>

<style lang="css">
</style>
