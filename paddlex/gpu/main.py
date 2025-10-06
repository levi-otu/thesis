from paddlex import create_pipeline
pipeline = create_pipeline(pipeline="doc_understanding")
output = pipeline.predict(
    {
        "image": "../book_of_proof_page_3.png",
        "query": "Identify/extract the contents of this file and output them in markdown format."
    }
)
for res in output:
    res.print()
    res.save_to_json("./output/")
    print(f"This is the visualized image in dict form: {res.img}")
