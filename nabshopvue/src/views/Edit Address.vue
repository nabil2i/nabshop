<template>
<div>
    <!-- <Navbar
      v-bind:user_data="user_data"/> -->

<div class="loginform2 container" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
    <div class="text-center mb-5">
        <h1 class="mt-4">Edit address</h1>
    </div>

    <form>

      
      <div class="form-floating mb-4">
        <input type="text" id="fullname" class="form-control" value="John Doe" />
        <label class="form-label" for="fullname">Full name</label>
      </div>

       <div class="form-floating mb-4">
        <input type="text" id="phone" class="form-control" value="123456789" />
        <label class="form-label" for="phone">Phone</label>
      </div>

       <div class="form-floating mb-4">
        <input type="text" id="country" class="form-control" value="Africa"/>
        <label class="form-label" for="country" placeholder>Country</label>
      </div>

       <div class="form-floating mb-4">
        <input type="text" id="city" class="form-control" value="Doe" />
        <label class="form-label" for="city">City</label>
      </div>

       <div class="form-floating mb-4">
        <input type="text" id="street" class="form-control" value="Xitucheng Road" />
        <label class="form-label" for="street">Street</label>
      </div>

       <div class="form-floating mb-4">
        <input type="text" id="building" class="form-control" value="10 Xitucheng Road" />
        <label class="form-label" for="building">Building</label>
      </div>

       <div class="form-floating mb-4">
        <input type="number" id="zipcode" class="form-control" value="4200" />
        <label class="form-label" for="zipcode">Zip code</label>
      </div>

      <button type="submit" class="btn btn-success btn-block btn-nabshop mb-4">Save</button>
    </form>
  </div>

</div>
</template>

<script>
export default {
  name: 'EditAddress',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.btn-nabshop {
  width: 100%;
}

.loginform2 {
  width: 700px;
  height: min-content;
  border: 2px;
  border-radius: 7px;
  background: rgb(219, 217, 217);
  padding: 20px 40px;
  margin-top: 50px
}


</style>
