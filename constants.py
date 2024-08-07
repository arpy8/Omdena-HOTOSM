import json

PAGE_BANNER = "assets/images/banner.png"
PAGE_FAVICON = "assets/images/favicon.png"
PAGE_BACKGROUND = "assets/images/background.png"


HOME_PAGE_DESCRIPTION = """
<div class="home">
    <!-- <h3>Executive Summary</h3> -->
    <p class="description">
      In the past, we embarked on a collaborative endeavor to construct an
      open-source, AI-assisted mapping tool in partnership with the Humanitarian
      OpenStreetMap Team (HOT) and Omdena. This initiative was designed to harness
      the potential of AI to bolster the capabilities of global open mapping
      initiatives by empowering end users to craft and refine AI models for
      feature extraction directly within a live environment. Our primary focus
      rested on the development of models for binary and multi-semantic
      segmentation on open aerial imagery. To accomplish this, we leveraged
      training datasets comprising both raster and vector data, facilitating
      comprehensive model training and validation. Through concerted efforts and
      collaboration, we endeavored to democratize the process of mapping and
      enhance accessibility to critical geographical information for humanitarian
      and developmental purposes.
    </p>
    <h3>The Problem</h3>
    <p>
      Updating and enhancing global maps with detailed geographic and
      infrastructural features is a process fraught with challenges, primarily due
      to its reliance on time-consuming and resource-intensive manual methods.
      This traditional approach to mapping, which involves manually identifying
      and cataloging changes in the landscape, is not only slow but also prone to
      inaccuracies. As a result, the availability of up-to-date and accurate
      geographic data is often limited, creating significant hurdles for effective
      decision-making and response strategies across various critical sectors,
      including disaster management, urban development, and environmental
      protection.
      <br />
      <br />
      The impact of these challenges is profound. In disaster response scenarios,
      for instance, the absence of timely and precise map updates can severely
      impede rescue and relief operations, potentially exacerbating the
      vulnerability of affected populations. For urban planning and development
      initiatives, reliance on outdated maps can lead to inefficient resource
      allocation, planning errors, and overlooked opportunities for sustainable
      development. Similarly, environmental monitoring and conservation efforts
      suffer when changes in natural resources and land use cannot be quickly and
      accurately mapped, hindering actions aimed at protecting ecosystems and
      biodiversity.
      <br />
      <br />
      In light of these challenges, there is a pressing need for innovative
      solutions that can accelerate the mapping process, enhance the accuracy of
      the data collected, and ensure that comprehensive, up-to-date geographic
      information is readily accessible. This is where the collaborative
      initiative between the Humanitarian OpenStreetMap Team (HOT) and Omdena to
      develop an open-source, AI-assisted mapping tool comes into action. The
      project seeks to address a significant challenge in the field of global
      mapping: the labor-intensive and slow process of manually updating maps with
      detailed geographic and infrastructural features. By leveraging AI for
      feature extraction from aerial imagery, this project aims to transform the
      global mapping landscape, making it possible to rapidly update maps with
      high levels of precision and significantly improving accessibility to
      critical geographic data.
    </p>
    <h3>The Goal</h3>
    <p>
      The ultimate goal of this project was to enhance the capabilities of the AI-assisted mapping tool, enabling end users to efficiently create, train, and deploy AI models for feature extraction from aerial and drone imagery. This initiative aimed to significantly improve the quality and accessibility of open data, supporting a wide range of applications from urban planning to environmental monitoring.
      <br>
      The main goals of this challenge were:
      <ol>
          <li><b>Development of AI Models for Advanced Feature Extraction</b>: The project focused on expanding the AI models’ capabilities, testing various models such as Segment Anything (SAM), FastSAM, GroundingDINO (DINO + SAM), and Yolov8 + SAM, among others suggested by AI challenge collaborators. This involved leveraging cutting-edge machine learning algorithms and techniques to enhance the tool’s ability to accurately identify and extract features from complex imagery.</li>
          <li><b>Creation of Comprehensive Training Datasets</b>: Developing training datasets was a critical task, utilizing Open Aerial Map imagery and OpenStreetMap (OSM) data. This goal ensured that the AI models were trained on high-quality, diverse datasets that reflected the real-world complexity of geographic features.</li>
          <li><b>Evaluation of Model Performance</b>: The project rigorously evaluated the performance of each model based on precision, recall, and other relevant metrics. This systematic assessment aimed to identify the most effective models for feature extraction, ensuring that the tool met high standards of accuracy and reliability.</li>
          <li><b>Ensuring Open Access and Collaboration</b>: All libraries and dependencies used in the project were free and open source, and the datasets were public, provided by the partner. This approach promoted collaboration within the community and ensured that the project’s outcomes were accessible to a wide audience.</li>
      </ol>
      By achieving these goals, this project delivered a powerful, user-friendly tool that democratized access to advanced AI capabilities for feature extraction from aerial and drone imagery. This initiative not only advanced the state of open mapping initiatives but also empowered users across various sectors to leverage AI for creating more accurate, up-to-date maps, thereby facilitating informed decision-making and innovation in addressing global challenges.
    </p>
</div>
"""


with open("./assets/data.json", "r") as f:
    TASKS_DICT = json.load(f)
    TASKS_DICT = {k: v for k, v in TASKS_DICT.items()}
    
if __name__=="__main__":
    print(TASKS_DICT.keys())