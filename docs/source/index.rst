Welcome to the advISO Guide Series!
===================================

The advISO Project
------------------
The advISO project has developed a modular framework to guide laboratories in achieving international bioinformatics accreditations.

advISO provides practical tools and training resources to support medical laboratories, especially in low- and middle-income countries, to achieve ISO 15189 and ISO 17025 accreditation.

The freely available and accessible modular framework resources can be used independently or as part of a lab's ISO accreditation journey.

The challenges
---------------

Bioinformatics is a relatively new modality in medical laboratories. It is a digital, rather than a laboratory discipline. This creates tangible issues when bioinformatics must be integrated into ISO 15189 or 17025 processes that are designed from a laboratory perspective.

We have identified a set of significant challenges that are holding back the
development of bioinformatics approaches within accredited labs:

.. raw:: html

   <style>
     .bm { position: relative; height: 640px; margin: 1.5rem 0; }
     .bm svg { position: absolute; left: 0; top: 0; pointer-events: none; }
     .bm line { stroke: var(--c); stroke-width: 3; stroke-linecap: round;
                opacity: .5; transition: opacity .2s, stroke-width .2s; }
     .bm line.on { opacity: 1; stroke-width: 5; }
     .bm.hovering line:not(.on) { opacity: .15; }

     .bm-node { position: absolute; width: 27%; box-sizing: border-box;
                transform: translate(-50%, -50%); padding: .7rem .9rem;
                font-size: .88rem; line-height: 1.4;
                background: rgba(127,127,127,.1); border: 1px solid rgba(127,127,127,.3);
                border-top: 5px solid var(--c); border-radius: 8px;
                transition: box-shadow .2s, background .2s; }
     .bm-node:hover, .bm-node:focus { background: rgba(127,127,127,.2);
                box-shadow: 0 2px 12px rgba(0,0,0,.25); outline: none; }
     .bm-node strong { display: block; margin-bottom: .2rem; color: var(--c); }

     .bm-centre { left: 50%; top: 50%; width: 22%; z-index: 2; text-align: center;
                  font-weight: 700; font-size: 1rem; padding: 1.3rem 1rem;
                  border: 3px solid #3b82f6; border-radius: 50%; }

     @media (max-width: 760px) {
       .bm { height: auto; display: flex; flex-direction: column; gap: .8rem; }
       .bm svg { display: none; }
       .bm-node, .bm-centre { position: static !important; transform: none !important;
                              width: auto !important; }
       .bm-centre { order: -1; border-radius: 12px; }
     }
   </style>

   <div class="bm" id="bm1">
     <svg aria-hidden="true"></svg>

     <div class="bm-node bm-centre">Challenges for bioinformatics in accredited labs</div>

     <div class="bm-node bm-branch" tabindex="0" style="--c:#ef4444">
       <strong>Language and processes</strong>
       Differences between bioinformatics language and processes and those used in the wet-lab
     </div>
     <div class="bm-node bm-branch" tabindex="0" style="--c:#f59e0b">
       <strong>Competency and training</strong>
       Different competency and training requirements for bioinformatics staff at all career stages
     </div>
     <div class="bm-node bm-branch" tabindex="0" style="--c:#10b981">
       <strong>Validation and verification</strong>
       Different requirements, particularly with respect to dataset building
     </div>
     <div class="bm-node bm-branch" tabindex="0" style="--c:#8b5cf6">
       <strong>Auditing and assessment</strong>
       Different requirements, particularly with respect to the use of software and databases
     </div>
     <div class="bm-node bm-branch" tabindex="0" style="--c:#ec4899">
       <strong>Fixing and updating</strong>
       Different considerations in terms of fixing issues and updating software and databases
     </div>
     <div class="bm-node bm-branch" tabindex="0" style="--c:#06b6d4">
       <strong>Pace of innovation</strong>
       Its impact on the evolution and iteration of processes used to deliver services
     </div>
   </div>

   <script>
     (function () {
       var bm = document.getElementById("bm1"),
           svg = bm.querySelector("svg"),
           centre = bm.querySelector(".bm-centre"),
           nodes = bm.querySelectorAll(".bm-branch"),
           lines = [];

       nodes.forEach(function (n) {
         var l = document.createElementNS("http://www.w3.org/2000/svg", "line");
         l.style.setProperty("--c", n.style.getPropertyValue("--c"));
         svg.appendChild(l); lines.push(l);
         function on()  { bm.classList.add("hovering");    l.classList.add("on"); }
         function off() { bm.classList.remove("hovering"); l.classList.remove("on"); }
         n.addEventListener("mouseenter", on); n.addEventListener("mouseleave", off);
         n.addEventListener("focus", on);      n.addEventListener("blur", off);
       });

       function layout() {
         var W = bm.clientWidth, H = bm.clientHeight;
         svg.setAttribute("width", W); svg.setAttribute("height", H);
         if (W < 760) return;                          // stacked fallback via CSS
         var cx = W / 2, cy = H / 2, rx = W * 0.37, ry = H * 0.38,
             a = centre.offsetWidth / 2, b = centre.offsetHeight / 2;

         nodes.forEach(function (n, i) {
           var ang = -Math.PI / 2 + i * 2 * Math.PI / nodes.length,
               nx = cx + rx * Math.cos(ang), ny = cy + ry * Math.sin(ang),
               dx = nx - cx, dy = ny - cy;
           n.style.left = nx + "px"; n.style.top = ny + "px";

           // start on the centre ellipse, end on the node's rectangle edge
           var t0 = 1 / Math.sqrt((dx / a) * (dx / a) + (dy / b) * (dy / b)),
               t1 = 1 / Math.max(Math.abs(dx) / (n.offsetWidth / 2),
                                 Math.abs(dy) / (n.offsetHeight / 2)),
               l = lines[i];
           l.setAttribute("x1", cx + dx * t0); l.setAttribute("y1", cy + dy * t0);
           l.setAttribute("x2", nx - dx * t1); l.setAttribute("y2", ny - dy * t1);
         });
       }

       layout();
       window.addEventListener("resize", layout);
       window.addEventListener("load", layout);
     })();
   </script>

Our guides
-------------

We have created a set of modular guides that are intended to be used independently or together to support laboratories in achieving bioinformatics accreditation. The guides are designed to be practical and accessible, providing step-by-step instructions and resources to help laboratories navigate the accreditation process. They are not intended to be a set of instructions for achieving accreditation, but rather a set of resources to support laboratories in their accreditation journey.



.. grid:: 2
   :gutter: 3

   .. grid-item::

      .. image:: _static/sop_guide_button_horizontal.png
         :target: https://adviso-sop-guide.readthedocs.io/en/latest/
         :alt: advISO SOP Guide
         :width: 100%
         :align: center
         :class: guide-button

   .. grid-item::

      .. image:: _static/competency_guide_button_horizontal.png
         :target: https://adviso-competency-guide.readthedocs.io/en/latest/
         :alt: advISO Competency Guide
         :width: 100%
         :align: center
         :class: guide-button

   .. grid-item::

      .. image:: _static/validation_guide_button_horizontal.png
         :target: https://adviso-validation-guide.readthedocs.io/en/latest/
         :alt: advISO Validation Guide
         :width: 100%
         :align: center
         :class: guide-button

   .. grid-item::

      .. image:: _static/audit_guide_button_horizontal.png
         :target: https://adviso-audit-guide.readthedocs.io/en/latest/
         :alt: advISO Audit Guide
         :width: 100%
         :align: center
         :class: guide-button

   .. grid-item::

      .. image:: _static/glossary_button_horizontal.png
         :target: https://adviso-glossary.readthedocs.io/en/latest/
         :alt: advISO Glossary
         :width: 100%
         :align: center
         :class: guide-button

Our People
-----------
The advISO project is led by Cardiff University, in collaboration with Public Health Wales, Wellcome Sanger Institute, South African National Bioinformatics Institute, and University of the Western Cape. The project team includes experts in bioinformatics, laboratory accreditation, and training.

Project Leads
=============


.. grid:: 1 2 3 3
   :gutter: 3

   .. grid-item-card:: Professor Tom Connor
      :text-align: center

     
      Tom is Professor of Bioinformatics and Microbial Genomics at Cardiff University's School of Biosciences and Head of the Public Health Genomics Unit at Public Health Wales. 



   .. grid-item-card:: Professor Alan Christoffels
      :text-align: center


      Alan is Director of the South African Medical Research Council Bioinformatics Unit and plays a key role in engaging institutes and organisations to join the project as pilot sites. 


   .. grid-item-card:: Dr Dominique Anderson
      :text-align: center
      
      Dominique, as Senior Researcher and Biocollection Informatics Team Lead at the South African National Bioinformatics Institute, contributes to the project by supporting training, delivery, engagement, and resource testings. 

   .. grid-item-card:: Dr Alice Matimba
      :text-align: center

      Alice, as Head of Training and Global Capacity at Wellcome Connecting Science, is leading the training component of the project. 

   .. grid-item-card:: Dr Kevin Howe
      :text-align: center

      Kevin is leading the Malaria work on the project, within his role as Head of Analysis Ready Data at the Wellcome Sanger Institute.

   .. grid-item-card:: Peter van Heusden
      :text-align: center

      Peter, a Senior Bioinformatician at the South African National Bioinformatics Institute, is leading the tuberculosis efforts of the project.


Project Team Members
====================

.. grid:: 1 2 3 3
   :gutter: 3

   .. grid-item-card:: Dr Rebecca Williams
      :text-align: center

      Rebecca is the advISO project manager. She combines her scientific expertise with project management skills to ensure research projects are delivered successfully from inception to completion.

   .. grid-item-card:: Dr Ashley Sendell-Price
      :text-align: center

      Ashley is a bioinformatician based at Public Health Wales and is developing templates and validation datasets for the project resources. He brings ISO 15189:2022 awareness training from UKAS. 

   .. grid-item-card:: Amy Gaskin
      :text-align: center

      Amy is a bioinformatician based at Public Health Wales and is developing templates and validation datasets for the project resources. She brings ISO 15189:2022 awareness training from UKAS.

   .. grid-item-card:: Edgar Chimuka
      :text-align: center

      Edgar is the systems administrator based at the South African National Bioinformatics Institute. His expertise includes managing and supporting Linux environments, server infrastructure, virtualisation platforms, monitoring solutions, and automation frameworks.

   .. grid-item-card:: Sophia Bam
      :text-align: center

      Sophia's role on the project as the Senior training co-ordinator based at the South African National Bioinformatics Institute is to develop and deliver training resources for the project.

   .. grid-item-card:: Buhle Ntozini
      :text-align: center

      Buhle is a bioinformatics developer at the South African National Bioinformatics Institute providing key deliverables on tuberculosis aspects of the project.

   .. grid-item-card:: Sibongiseni Msipa
      :text-align: center

      Sibongiseni, as the project's junior training coordinator at the South African National Bioinformatics Institute, is supporting the development and delivery of training courses for the project.
     
   .. grid-item-card:: Tichaona Machiya
      :text-align: center

      Tichaona is the project's Bioinformatics and Genomics Training Development Officer based at Cardiff University.


Project Information
---------------------

These guides have been produced as part of the Wellcome Trust-funded project: *ISO in a Box: Developing a framework to enable the development of end-to-end genomics-based ISO 15189 and ISO 17025 accredited services, anywhere in the world* (Grant Reference: 228162/Z/23/Z). The project is led by Cardiff University, in collaboration with Public Health Wales, Wellcome Sanger Institute, South African National Bioinformatics Institute, and University of the Western Cape.

Find out more about the `advISO Bioinformatics accreditation in a box project <https://www.cardiff.ac.uk/adviso-bioinformatics-accreditation>`_.

.. figure:: ./_static/partner_logos.png
        :align: center
        :width: 650px
