<template>
<div>

  <div class="loginform2 container" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
    <div class="text-center mb-5">
        <h1 class="mt-4">Change password</h1>
    </div>

    <form>

      <!-- Password input -->
      <div class="form-floating mb-4">
        <input type="password" id="loginPassword" class="form-control" />
        <label class="form-label" for="loginPassword">Current assword</label>
      </div>

      <!-- Password input -->
      <div class="form-floating mb-4">
        <input type="password" id="loginPassword" class="form-control" />
        <label class="form-label" for="loginPassword">New assword</label>
      </div>

      <div class="form-floating mb-4">
        <input type="password" id="loginPassword" class="form-control" />
        <label class="form-label" for="loginPassword">Confirm new password</label>
      </div>
      <!-- Submit button -->
      <button type="submit" class="btn btn-success btn-block btn-nabshop mb-4">Save</button>
    </form>
  </div>

</div>
</template>

<script>
export default {
  name: 'ChangePassword',
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
