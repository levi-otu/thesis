from paddlex import create_pipeline

pipeline = create_pipeline(pipeline="PP-StructureV3")

output = pipeline.predict(
    input="../../book_of_proof_page_3.png",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False,
)
for res in output:
    res.print() ## Print the structured prediction output
    res.save_to_json(save_path="output") ## Save the structured JSON result of the current image
    res.save_to_markdown(save_path="output") ## Save the result of the current image in Markdown format
