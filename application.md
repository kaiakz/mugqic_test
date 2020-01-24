# Application for GSOC 2020
--------------------------------

# General

## Why does your org want to participate in Google Summer of Code?

[text limitation to 1000 charaters - so I shorten it]
Next-generation sequencing and other high-throughput technologies are revolutionizing life sciences and health care research. Data processing and interpretation, rather than data production, has become the major limiting factor for discovery and innovation. In this context, bioinformatics has become an indispensable technology across the life sciences that must be made readily available. To better address this growing demand for bioinformatics, the Canadian Centre for Computational Genomics (C3G) provides bioinformatics analytical resources to the community.

In this context, we have been developing a suite of open source bioinformatics analysis pipelines: https://bitbucket.org/mugqic/genpipes . These pipelines need to constantly evolve to stay up-to-date with changes in genomic technologies. We believe that this represents a rich source of potential projects for GSoC students and, conversely, we think that having students working on these projects will be very helpful to us.


## How many potential mentors have agreed to mentor this year?
[WE MENTOR MENTORS?]

6-10


## How will you keep mentors engaged with their students?

We expect our mentors to be motivated to stay engaged with their students throughout GSoC.
The main reason why is that mentors volunteer their time to create standard operating procedures and to develop methodological concept that led to the actual project proposals on our wiki page, and they are also looking for students to help them write code, tests, and documentation.
We already have weekly group meetings and we will ask all mentors to give updates on GSoC projects at those meetings.

## How will you help your students stay on schedule to complete their projects?

First, student will need to provide a detailed timeline in their project proposals.
Second, we will require weekly calls between mentors and students, in order to provide efficient support to student with their projects.
If needed, we will adjust the projects to avoid roadblocks and ensure that they can be completed within the time-frame.

## How will you get your students involved in your community during GSoC?

*NOT SURE IF LINKS ARE ALLOWED HERE*
*1000 character max- I shortened the text*

We expect our GSoC students to be already involved via college or university courses that involve Next Generation Sequencing, python or R.

We will minimize direct conversations between students and mentors and we will strongly encourage them to use the GenPipes google group or our mailing list. 

We will also encourage them to discuss on specific community forums like biostar or seqanswers.
We think students should interact with the whole community in order to increase the knowledge transmission.

During the GSoC process we want clear evidence that the student is motivated. This will include providing accurate selection test results, installing our software, training with test data,  asking questions and planning their project. 


Finally, the student code will be developed in separate git branches. If the work is successful it will be merged to the master branch. The merge requests are reviewed and commented by the other member of the community


## How will you keep students involved with your community after GSoC?

*TOO VAGUE: MORE DETAILS/IDEAS? Is it better now*
*1000 character max- I shortened the text*

We will strongly encourage our GSoC students to continue to be involved in the community and to get involved in the future development of our software.

Students' contribution will be clearly identified. We expect that student will stay implicated in the project in order to maintain and support their valuable contribution. We will strongly encourage students to answer questions or comments regarding the code they developed even after the completion of the project. 

We think students will enjoy working with us and we hope that the work they will done during the GSoC could be use in the student future studies.

We organize regular workshops to explain our tools and we will encourage GSoC students to participate in those workshops. We also plan to set-up monthly user web-meeting and we will strongly encourage student to take part of it even after the completion of the project.

Finally it would be nice if some student could become mentors for futur GSoC programs.


## Has your org been accepted as a mentoring org in Google Summer of Code before?

yes

## Which years did you participate?

2019
2018
2016

## For each year your organzsation has praticiped, provide the counts of successful and total students

2019 - 5 students - 4 successful students
2018 - 3 students - 3 successful students
2016 - 4 students - 3 successful students

## If your org has applied for GSoC before but not been accepted, select the years:
2017
2015

## If you are a new organization to GSoC, is there a Google employee or previously participating organization who will vouch for you? If so, please enter their name, contact email, and relationship to your organization.

NA

## Are you part of a foundation/umbrella organization?

We are part of Genome Canada, which is an organism that funds all genomics research in Canada.

##  What year was your project started ?

2011


## Where does your source code live ?
https://bitbucket.org/mugqic/genpipes


## Anything else we should know (optional)?

----------------------------

# Public Profile

## Website URL
http://computationalgenomics.ca/


## Tagline

Analytical solutions for Next-Generation Sequencing data

## Your organization logo. Must be a 24-bit PNG, minimum height 256 pixels.

[c3g](img/C3G_source_MB_H256.png)


## Primary Open Source License

GNU GENERAL PUBLIC LICENSE Version 3

## Organization Category

Science and Medicine

## Technology Tags
Python, R-project, Javascript, React, NodeJS

## Topic Tags
Bioinformatics, data science, visualization, statistics, Web Development.

## Ideas List

https://bitbucket.org/mugqic/gsoc_2020


# Descriptions

These descriptions will be displayed on the organization list page (Short Description) and on your organization's page (Long Description). More details.

The Long Description may include limited Markdown.

## Short Description
 
The Canadian Centre for Computational Genomics provides bioinformatics analysis and High Performance Computing services for the life science research community

## Long Description

The Montreal [C3G](http://computationalgenomics.ca/) node is hosted at the McGill University and Genome Quebec Innovation Center (MUGQIC).
The Montreal node is strongly involved with [GenAP](https://genap.ca/) and has developed several genomic data analysis pipelines.
Since 2011, we have completed more than 400 bioinformatics analysis projects with over 290 distinct groups of researchers across Canada.
Our teams have significant experience in personalized medicine applications.
These have included genome analysis and interpretation of personal genomes,
technology and services to record patient presentations, RNA- and ChIP-seq data analysis, and analysis of complete human epigenomes in both germline disorders and cancers.
Each year C3G co-organizes several international workshops about next-generation sequencing data analysis.

The Montreal C3G node develops the [GenPipes](https://bitbucket.org/mugqic/genpipes) pipelines which consist of Python scripts which create a list of jobs running Bash commands to analyze NGS data.
Those scripts support dependencies between jobs and a smart restart mechanism if some jobs fail during pipeline execution.
Job commands and parameters can be modified through several configuration files.
We currently maintain 7 pipelines and develop 3 others.

The Montreal C3G node also develops several bionformatics tools:
 
 * [BVAtools](https://bitbucket.org/mugqic/bvatools)
 * [POPsv](https://github.com/jmonlong/PopSV)
 * [SCoNEs](https://bitbucket.org/mugqic/scones)


---------------------------
 
# Proposals

Guidance for students on how to apply to your organization. Should include any prerequisites or requirements. You may wish to include a template or tips for their proposals. May include limited Markdown.

Enter tags that students can select (one) from and apply to their own proposals to help organize them. Examples: New Feature, Optimization. You can also use these to designate "sub-organizations" if you are an umbrella organization.

## Application Instructions

How to apply to our projects:   

    1 Look for a project that needs a student on https://bitbucket.org/mugqic/gsoc2020/overview
    2 Each project should have ?tests? students can complete to demonstrate relevant skills. After completing at least one test, please post your test results to a github/bitbucket repo, and add a link to your test results on the google group.
    3 Send an email to the mentors of the project. Include a link to your test results, and explain why you are interested in the project.
    4 **Do NOT submit any applications to google without getting approval from the mentors.** If the mentors judge that you are capable of the project, then they will respond and help you to write a proposal to submit to Google. It should include most of the details from the project proposal wiki page, and additionally a detailed timeline that explains your plan for writing code, documentation, and tests.
    5 Once your mentors have proof-read your proposal, submit it to google: https://summerofcode.withgoogle.com/                     

## Proposal Tags
Bioinformatics, pipeline development,  data science, visualization, statistics, genomics, genetics, web development


# Contact Methods

You must complete at least one of the following three contact options.

## IRC Channel


## Mailing List
gsoc@computationalgenomics.ca


## General Email
info@computationalgenomics.ca

-------------------------
# Links


## Google+ URL (optional)


## Twitter URL (optional)
https://twitter.com/C3Genomics

## Blog URL (optional)
https://groups.google.com/forum/#!forum/genpipes
