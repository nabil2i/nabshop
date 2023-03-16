<template>
<div>
<div class="loginform2 container" id="pills-login" role="tabpanel" aria-labelledby="tab-login">
    <div class="text-center mb-5">
        <h1 class="mt-4">Change name</h1>
    </div>

    <form>

      <div class="form-floating mb-4">
        <input type="text" id="first_name" class="form-control" value="John"/>
        <label class="form-label" for="first_name" placeholder>New first name</label>
      </div>

      
      <div class="form-floating mb-4">
        <input type="text" id="last_name" class="form-control" value="Doe" />
        <label class="form-label" for="last_name">New last name</label>
      </div>


      <button type="submit" class="btn btn-success btn-block btn-nabshop mb-4">Save</button>
    </form>
  </div>

</div>
</template>

<script>
export default {
  name: 'ChangeName',
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
