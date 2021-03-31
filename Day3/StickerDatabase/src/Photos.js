import React from 'react'
import { Grid } from "@material-ui/core"
import Card from "./Card"
import img1 from "./attachments/IMG-2726.jpg"
import img2 from "./attachments/IMG-2727.jpg"
import img3 from "./attachments/IMG-2728.jpg"
import img4 from "./attachments/IMG-2729.jpg"
import img5 from "./attachments/IMG-2730.jpg"
import img6 from "./attachments/IMG-2731.jpg"
import img7 from "./attachments/IMG-2732.jpg" 
import img8 from "./attachments/IMG-2733.jpg"
import img9 from "./attachments/IMG-2734.jpg"
import img10 from "./attachments/IMG-2735.jpg"
import img11 from "./attachments/IMG-2736.jpg"
import img12 from "./attachments/IMG-2737.jpg"
import img13 from "./attachments/IMG-2738.jpg"
import img14 from "./attachments/IMG-2739.jpg"


function Photos() {
    const imgs = [img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13,img14]
    return (
            <Grid container spacing={4} className="gridcontainer">
                {
                    imgs.map(img => (
                        <Grid item xs={12} sm={6} md={4}>
                        <Card img={img}/>
                </Grid>
                    ))
                }                
            </Grid>
    )
}

export default Photos
