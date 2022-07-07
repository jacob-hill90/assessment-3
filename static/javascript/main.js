office_list = [{'product':'Stapler','price':'12.19'}, {'product':'Label Maker','price':'35.59'}, {'product':'Printer','price':'119.99'}]

kitchen_list = [{'product':'Knife','price':'14.99'}, {'product':'Cutting Board','price':'13.59'}, {'product':'Toaster','price':'45.99'}]

garage_list = [{'product':'Wrench','price':'9.19'}, {'product':'Paint','price':'23.99'}, {'product':'Vice','price':'89.99'}]

livingroom_list = [{'product':'Lamp','price':'23.50'}, {'product':'Pillow','price':'13.99'}, {'product':'Rug','price':'30.99'}]

patio_list = [{'product':'Fountain','price':'122.19'}, {'product':'Plant','price':'25.99'}, {'product':'Bird Feeder','price':'20.99'}]

document.getElementById('search-form').addEventListener('submit', (event)=>{
    event.preventDefault()

    const searchInput = document.getElementById('product')
    console.log(searchInput.value)
})

