<template>
    <section class="h-100 h-custom">
      <div class="container cart-container h-100 py-5">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col">
            <h3 class="fw-normal mb-5 text-black">Order #{{ order.id }}</h3>

            <div class="table-responsive">
              <table class="table">
                <thead>
                  <tr>
                    <th scope="col" class="h5">Order details</th>
                    <th scope="col">Format</th>
                    <th scope="col">Unit Price</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Price</th>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="item in order.items"
                    v-bind:key="item.bookedition.id"
                    v-bind:initialItem="item">
                    <th scope="row">
                      <div class="d-flex align-items-center">
                        <img :src="item.bookedition?.book?.images[0]?.get_image"
                          style="width: 120px;" alt="Book">
                        <div class="flex-column ms-4">
                          <p class="mb-2">{{ item.bookedition?.book?.title }}</p>
                          <p class="mb-0">{{ item.bookedition?.book?.author }}</p>
                        </div>
                      </div>
                    </th>
                    <td class="align-middle">
                      <p class="mb-0" style="font-weight: 500;"><span></span>{{ item.bookedition.bookformat}}</p>
                    </td>
                    <td class="align-middle">
                      <p class="mb-0" style="font-weight: 500;"><span>$</span>{{ item.bookedition.unit_price}}</p>
                    </td>
                    <td class="align-middle">
                      <p class="mb-0" style="font-weight: 500;"><span></span>{{ item.quantity}}</p>
                    </td>
                    <td class="align-middle">
                      <p class="mb-0" style="font-weight: 500;"><span>$</span>{{ item.price}}</p>
                    </td>
                  </tr>
                </tbody>
              </table> 
            </div>
            <div class="d-flex justify-content-between" style="font-weight: 500;">
              <p class="mb-2">Total Paid</p>
              <p class="mb-2"> <strong><span>$</span>{{ order.total_amount}}</strong></p>
            </div>
            
            </div>
        </div>
      </div>
    </section>
</template>
<script>

export default {
  name: 'OrderSummary',
  props: {
    order: Object
  },
  components: {

  },
  data() {
    return {
    };
  },
  mounted() {
 
  },
  methods: {
  }
}
</script>

<style scoped lang="scss">
.cart-container {
  width: 900px
}
</style>
