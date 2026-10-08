\# Fictional Practice Rubric



This short rubric is for a portfolio exercise about consistent content review. It is intentionally fictional and does not represent an employer's or platform's policy.



\## Decision categories



\- \*\*allow\*\* — The example is clearly ordinary and benign.

\- \*\*needs\_review\*\* — Important context is missing or the wording is ambiguous, so a reviewer should not guess.

\- \*\*disallow\*\* — The example clearly asks for private credentials or unauthorized access to someone else's account.



These categories are deliberately narrow teaching examples. They are not universal labels.



\## Review steps



1\. Read the complete example and any context supplied with it.

2\. Base the decision only on the available evidence; do not invent missing details.

3\. Choose the closest category and give a brief rationale that points to the relevant wording.

4\. Use \*\*needs\_review\*\* when a missing fact could change the decision.

5\. Keep each `item\_id` unique and include a rationale for every row.



\## CSV format



The checker expects these headers:



```csv

item\_id,category,rationale

sample-001,allow,The message gives an ordinary study tip.

```



The script checks required columns, unique non-empty IDs, non-empty rationales, and category values. It does not decide whether a rationale is substantively correct.



\## Data and scope



All built-in examples are synthetic. Do not add private, employer, client, or production data to this demo. Follow the applicable written instructions and escalation process for any real review work.

