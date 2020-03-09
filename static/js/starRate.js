
// This class is using ES6 
class StarRate extends HTMLElement{
    // this function can height the star, para "index" which means how many stars we want to full
    highLight(index){
        for (let i =0;i < this.stars.length;i++){
                this.stars[i].classList.toggle('full',i <= index);
        }
    }

    //get value
    get value(){
        return this.getAttribute('value') || 0; //default is 0
    }

    //set value
    set value(val){
        this.setAttribute('value',val);
        this.highLight(this.value -1);
    }

    //get number of star
    get number(){
        return this.getAttribute('number') || 5; // return number which is write in html or 5
    }

    set number(num){
        this.setAttribute('number',num);
        this.stars = []   //creat a list of star
        while(this.firstChild){
            this.removeChild(this.firstChild)
        }
        for (let i = 0; i < this.number; i++) {
            let starDiv = document.createElement('div');
            starDiv.className = 'star';
            this.appendChild(starDiv);
            this.stars.push(starDiv);
        }
        //if use var to define i, it can be accessed outside of for loop
        //let can be only accessed in block such as for loop block
        
        //declare a value
        this.value = this.value;
    }
    constructor(){
        super()
         // this is just want to call the set method of the number,
         // the value of this.number on the right, is the default value of get
            this.number = this.number;  
         //=============== add hover listener=============
        this.addEventListener('mousemove',e =>{
        //getBoundingClientRect can get the position of this element block in the window[top, right, bottom, left]
        let bar = this.getBoundingClientRect();
        //startIndex can find which star is the mouse hover on.
            //e.pageX can get the X position of the mouse, relative with the document
            //(e.pageX - box.left) / box.with: got the percentage of the position
            //Math.floor ignore the float 4.1 will be 5
        let starIndex = Math.floor((e.pageX - bar.left) / bar.width * this.stars.length);
        this.highLight(starIndex);
    });
        //================ add mouse out listener ============
        this.addEventListener('mouseout', () => {
            //call the set value method
            this.value = this.value;
        });

        this.addEventListener('click', e => {
            let bar = this.getBoundingClientRect();
            let starIndex = Math.floor((e.pageX - bar.left) / bar.width * this.stars.length);
            this.value = starIndex +1;

            //create a event in order to save the rate
            let rateEvent = new Event('rated');
            this.dispatchEvent(rateEvent);
        });

    }
    

    
   
}

// Register our cunstom tag x-star-rating to the class StarRating
window.customElements.define('x-star-bar', StarRate);