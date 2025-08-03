'use client'

import React from "react";
import { helloWorldApi } from "@/api/helloWorldApi";

export default function Home() {

  React.useEffect(() => {
    alert("Hello, world! - Interactive Story Weaver")
    console.log(process.env.NEXT_PUBLIC_SERVER_API_URL)
    console.log("trying to fetch hello world")
    helloWorldApi()
      .then((result) => {
        console.log("helloWorldApi Result: ", result);
      })
      .catch((error) => {
        console.error("Error fetching hello world:", error);
      });
  }, []);
  return (
    <div> <h1> HELLO WORLD PAGE</h1></div>
  );
}
