<template>
  <div class="loginform container" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
    <div class="text-center mb-5">
      <div class="mt-4"><img src="../assets/nabshop-light.png" width="150" alt="" class=""></div>
        <h1 class="mt-4">Sign up</h1>
    </div>

    <form>

      <!-- <p class="text-center">or:</p> -->

      <!--Username input -->
      <div class="form-floating mb-4">
        <input type="text" id="userName" class="form-control" />
        <label class="form-label" for="userName">Username</label>
      </div>

      <!-- Email input -->
      <div class="form-floating mb-4">
        <input type="email" id="loginName" class="form-control" />
        <label class="form-label" for="loginName">Email</label>
      </div>

      <!-- Password input -->
      <div class="form-floating mb-4">
        <input type="password" id="loginPassword" class="form-control" />
        <label class="form-label" for="loginPassword">Password</label>
      </div>

      <!-- Password input -->
      <div class="form-floating mb-4">
        <input type="password" id="loginPassword" class="form-control" />
        <label class="form-label" for="loginPassword">Confirm Password</label>
      </div>

      <!-- 2 column grid layout -->
      <!-- <div class="row mb-4">
        <div class="col-md-6 d-flex justify-content-center">
         
          <div class="form-check mb-3 mb-md-0">
            <input class="form-check-input" type="checkbox" value="" id="loginCheck" checked />
            <label class="form-check-label" for="loginCheck"> Remember me </label>
          </div>
        </div>

        <div class="col-md-6 d-flex justify-content-center">
        
          <a href="#!">Forgot password?</a>
        </div>
      </div> -->

      <!-- Submit button -->
      <button type="submit" class="btn btn-success btn-block btn-nabshop mb-4">Continue</button>

      <!-- Register buttons -->
      <div class="text-center">
        <p>By creating an account, you agree to NabShop's Conditions of User and Privacy policy.</p>
        <p>Already have an account? <a href="/login">Log in</a></p>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'signupform',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.loginform {
  width: 400px;
  height: min-content;
  border: 2px;
  border-radius: 7px;
  background: rgb(219, 217, 217);
  padding: 20px 40px;
  margin-top: 50px
}

.btn-nabshop {
  width: 100%;
}


</style>
