<template>
     <b-container fluid>
    <b-row>
      <b-col md="12">
        <card>
          <template v-slot:headerTitle>
            <h4 class="card-title">Editable Table</h4>
          </template>
          <template v-slot:headerAction>
            <b-button variant="primary" @click="add">Add New</b-button>
          </template>
          <template v-slot:body>
            <b-row>
              <b-col md="12" class="table table-bordered table-responsive-md table-striped text-center">
                <b-table bordered hover :items="rows" :fields="columns" foot-clone>
                  <template v-slot:cell(name)="data">
                    <span v-if="!data.item.editable">{{ data.item.name }}</span>
                    <input type="text" v-model="data.item.name" v-else class="form-control">
                  </template>
                  <template v-slot:cell(age)="data">
                    <span v-if="!data.item.editable">{{ data.item.age }}</span>
                    <input type="text" v-model="data.item.age" v-else class="form-control">
                  </template>
                  <template v-slot:cell(companyname)="data">
                    <span v-if="!data.item.editable">{{ data.item.companyname }}</span>
                    <input type="text" v-model="data.item.companyname" v-else class="form-control">
                  </template>
                  
                  <template v-slot:cell(country)="data">
                    <span v-if="!data.item.editable">{{ data.item.country }}</span>
                    <input type="text" v-model="data.item.country" v-else class="form-control">
                  </template>
                  <template v-slot:cell(city)="data">
                    <span v-if="!data.item.editable">{{ data.item.city }}</span>
                    <input type="text" v-model="data.item.city" v-else class="form-control">
                  </template>
                  <template v-slot:cell(sort)>
                    <span class="table-up"><a href="#!" class="indigo-text"><i class="fas fa-long-arrow-alt-up" aria-hidden="true"></i></a></span>
                     <span class="table-down"><a href="#!" class="indigo-text"><i class="fas fa-long-arrow-alt-down" aria-hidden="true"></i></a></span>
                  </template>
                  <template v-slot:cell(action)="data">
                    <b-button variant=" btn bg-primary-light btn-rounded btn-sm my-0" size="sm" @click="edit(data.item)" v-if="!data.item.editable">Edit</b-button>
                    <b-button variant=" btn bg-success-light btn-rounded btn-sm my-0" size="sm" @click="submit(data.item)" v-else>Done</b-button> 
                    <b-button variant=" btn bg-danger-light btn-rounded btn-sm my-0" size="sm" @click="remove(data.item)">Remove</b-button>
                  </template>
                </b-table>
              </b-col>
            </b-row>
          </template>
        </card>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
    name:'EditTable',
    methods: {
    add () {
      const obj = this.default()
      this.rows.push(obj)
    },
    default () {
      return {
        id: this.rows.length,
        name: '',
        age: '',
        companyname: '',
        country: '',
        city: '',
        editable: false
      }
    },
    edit (item) {
      item.editable = true
    },
    submit (item) {
      item.editable = false
    },
    remove (item) {
      const index = this.rows.indexOf(item)
      this.rows.splice(index, 1)
    }
  },
  data () {
    return {
      columns: [
        { label: 'Name', key: 'name', class: 'text-center' },
        { label: 'Age', key: 'age', class: 'text-center' },
        { label: 'Company Name', key: 'companyname', class: 'text-center' },
        { label: 'Country', key: 'country', class: 'text-center' },
        { label: 'City', key: 'city', class: 'text-center' },
        { label: 'Sort', key: 'sort', class: 'text-center' },
        { label: 'Remove', key: 'action', class: 'text-center' }
      ],
      rows: [
        {
         id: 1,
         name: 'Gio Metric',
         age: '25',
         companyname: 'Deepends',
         country: 'Spain',
         city: 'Madrid',
         editable: false
        },
        {
         id: 2,
         name: 'Manny Petty',
         age: '45',
         companyname: 'Insectus',
         country: 'France',
         city: 'San Francisco',
         editable: false
        },
        {
         id: 3,
         name: 'Lucy Tania',
         age: '26',
         companyname: 'Isotronic',
         country: 'Germany',
         city: 'Frankfurt am Main',
         editable: false
        },
        {
         id: 4,
         name: 'Anna Mull',
         age: '35',
         companyname: 'Portica',
         country: 'USA',
         city: 'Oregon',
         editable: false
        }
      ]
    }
  }
}
</script>